from django.contrib import admin
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.template import RequestContext

from market.api import models


class AccountAdmin(admin.ModelAdmin):
    """
    Account Admin
    """
    list_display = ('first_name', 'last_name', 'email', 'balance', 'is_active', 'is_staff', 'is_superuser', 'is_system')
    list_filter = ('balance', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    actions = ['apply_fine']
    icon = '<i class="material-icons">account_circle</i>'

    def apply_fine(self, request, queryset):
        form = None

        if 'apply' in request.POST:
            form = FineForm(request.POST)

            if form.is_valid():
                product = form.cleaned_data['product']
                for account in queryset:
                    account.apply_fine(product)
                self.message_user(request, "Fine applied to selected accounts")
                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = FineForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        opts = self.model._meta
        app_label = opts.app_label

        context = {'accounts': queryset, 'product_form': form, 'opts': opts, 'app_label': app_label}
        return render_to_response('admin/apply_fine.html', context, RequestContext(request))

