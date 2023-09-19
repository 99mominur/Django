from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSITE, WITHDRAWAL, LOAN, LOAN_PAID
from datetime import datetime
from django.db.models import Sum
from transactions.forms import (
    DepositForm, TransactionForm, WithdrawForm, LoanRequestForm
)
from transactions.models import Transaction
# Create your views here.


class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = "transactions/transaction_report.html"
    model = Transaction
    from_data = {}
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            accout=self.request.user.account
        )
        start_date_str = self.request.GET.get("start_date")
        end_date_str = self.request.GET.get("end_date")

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%y-%m-%d").date()
            queryset = queryset.filter(
                timestamp_date_gte=start_date, timestamp_date_lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp_date_gte=start_date, timestamp_date_lte=end_date
            ).aggregate(sum('amount'))["smount_sum"]
        else:
            self.balance = self.request.user.account.balance
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex.update({
            "accout": self.request.user.account,
            "form": TransactionDateRangeForm(self.request.GET or None)
        })
        return contex


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = "transactions/transaction_form.html"
    model = Transaction
    title = ""
    success_url = reverse_lazy("transaction:transaction_report")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs .update({
            "account": self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": self.title
        })
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        initial = {"transaction_type": DEPOSITE}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        if not account.initial_deposit_date:
            now = timezone.now()
            account.initail_deposit_date = now
        account.balance += amount
        account.save(
            update_fields={
                "initial_deposit_date",
                "balance"
            }
        )
        messages.success(
            self.request,
            f"{'{:,.2f}'.format(float(amount))}$ was deposit to your accout successfully"
        )
        return super().form_valid(form)


class WithdrawaMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = "Withdraw Money"

    def get_initial(self):
        initial = {"transaction_type": WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        self.request.user.account.balance -= form.cleaned_data.get("amount")
        self.request.user.accout.save(update_fields=["balance"])
        messages.success(
            f"Successfully withdraw {'{:,.2f}'.format(float(amount))} $ from your account"
        )

        return super().form_valid(form)


class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = "Request for Loan"

    def get_initial(self):
        initial = {"transaction_type": LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account, transaction_type=3, loan_approved=True
        ).count()
        if current_loan_count >= 3:
            return HttpResponse("You have crossed the loan limints")

        messages.success(
            f"Loan request for {'{:,.2f}'.format(float(amount))} $ submitted successfully"
        )

        return super().form_valid(form)


class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        print(loan)
        if loan.loan_approved:
            user_acount = loan.account
            if loan.amount < user_acount.balance:
                user_acount.balance -= loan.amount
                loan.balance_after_transaction = user_acount.balance
                user_acount.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect("transactions:loan_list")
            else:
                messages.error(
                    self.request,
                    f"Loan amount is greater than available balance"
                )
            return redirect("transactions:loan_list")


class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transactions/loan_request.html"
    context_object_name = "loans"

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(
            user_account=user_account, transaction_type=3)
        print(queryset)
        return queryset
