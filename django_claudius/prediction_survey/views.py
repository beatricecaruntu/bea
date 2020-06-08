from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from django_claudius.models import Case
from .form import CaseForm, Page1Form, Page2Form

# Global
MAX_PAGES = 2

# Return correct form given page number or none if invalid page_num
def _get_form_object(page_num):
        form_dict = {1: Page1Form,
                     2: Page2Form}
        return form_dict[page_num]

@login_required(login_url='/dashboard')
def serve_prediction_survey(request, page_num, case_id=None):
        if request.method == "POST":
                # New case if no case_id provided
                if case_id is None:
                        form = _get_form_object(page_num)(request.POST)
                # Update old case
                else:
                        case = Case.objects.get(pk=case_id)
                        form = _get_form_object(page_num)(request.POST, instance=case)
                # Form submit is valid
                if form.is_valid():
                        case = form.save()

                        # Set case owner to currently logged in user (only applicable to new cases but doesn't hurt)
                        if request.user.is_authenticated:
                                case.owner = request.user
                                case.save()

                        # Load next screen / dashboard
                        if page_num >= MAX_PAGES:
                                return redirect('dashboard')
                        return redirect('prediction_survey_index', page_num + 1, case.id)



        else:
                if case_id is None:
                        form = _get_form_object(page_num)()
                else:
                        case = Case.objects.get(pk=case_id)
                        form = _get_form_object(page_num)(instance=case)

        return render(request, 'prediction_survey/index.html', {'form': form,
                                                                'page_num': page_num,
                                                                'case_id': case_id})