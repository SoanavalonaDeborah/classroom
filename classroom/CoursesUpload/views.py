from django.shortcuts import render, redirect
from.models import UploadPDF
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from.forms import SupportCoursForm
from .models import SupportCours

def InformationsPDF(request):
    if request.method == 'POST':
        form = SupportCoursForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre les données dans la base de données
            return redirect('upload-pdf/')  # Redirige vers une page de succès
    else:
        form = SupportCoursForm()
    return render(request, 'infosPDF.html', {'form': form})


def UploadPDFform(request):
    if request.method == 'POST':
        document = UploadPDF(titre=request.POST['titre'], document=request.FILES['document'])
        document.save()
        return HttpResponseRedirect('success/')
    else:
        return render(request, 'upload.html')  # Assurez-vous que 'upload.html' est le nom de votre template


def SuccessPage(request):
    return render(request, 'success.html')


def InformationsPDFList(request):
    # Récupère tous les supports de cours
    support_cours_list = SupportCours.objects.all()
    return render(request, 'support_cours_list.html', {'support_cours_list': support_cours_list})


def download_pdf(request, course_id):
    try:
        support_cours = SupportCours.objects.get(id=course_id)
        if support_cours.pdf_file:
            return FileResponse(open(support_cours.pdf_file, 'rb'), as_attachment=True, filename=support_cours.pdf_file.split('/')[-1])
        else:
            return HttpResponse("No PDF found for this course.", status=404)
    except SupportCours.DoesNotExist:
        return HttpResponse("Course not found.", status=404)




