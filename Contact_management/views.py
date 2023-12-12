from django.shortcuts import render, redirect
from Contact_management.models import contacts
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
	data = contacts.objects.all()
	context = {"contactList" : data}
	print("daataa", data)
	return render(request, 'home.html', context)

def create_contact(request):
	
	if request.method == 'POST':
		name=request.POST['name']
		email=request.POST['email']
		notes=request.POST['notes']

		if check_if_contact_exists("create_contact", "", email):
			messages.error(request, "Duplicate Contact With Same Email Id Exists")
			return render(request ,"create_contact.html")

		new_contact = contacts(name=name, email=email, notes=notes, time=datetime.now())
		new_contact.save()
		messages.success(request, "Contact Created!")
		return redirect("home")

	return render(request,"create_contact.html")

def update_contact(request, con_id):
	contact_record = contacts.objects.get(id = con_id)
	
	if request.method == 'POST':
		contact_record.name=request.POST['name']
		contact_record.email=request.POST['email']
		contact_record.notes=request.POST['notes']

		if check_if_contact_exists("update_contact", con_id, contact_record.email):
			context = {"contact_record" : contact_record}

			messages.error(request, "Duplicate Contact With Same Email Id Exists")
			return render(request ,"update_contact.html", context)
		
		contact_record.save()	
		messages.success(request, "Contact Updated!")
		return redirect("home")
	
	return render(request,"update_contact.html", {"contact_record" : contact_record})


def delete_contact(request, con_id):
	contact_record = contacts.objects.get(id = con_id)
	if request.method == 'POST':
		print(">>>>>>>>>>>delete>>>>>>")
		contact_record.delete()
		messages.success(request, "Contact Deleted!")

		return redirect("home")
		
	return render(request, "delete_contact.html",{'contact_name': contact_record.name })
	
def contact_details(request, con_id):
	contact_record = contacts.objects.get(id = con_id)
	if request.method == 'POST':
		print(">>>>>>>>>>>detail>>>>>>")
		contact_record.delete()
		return redirect("home")

	return render(request, "contact_details.html", {"contact_record" : contact_record})
	


# def check_if_contact_exists(operation, contact_id, contact_email):
# 	if operation == "create_contact" and contacts.objects.filter(email = contact_email):
# 		print('exists')
# 		return True
# 	elif operation == "update_contact" and contacts.objects.filter(email = contact_email).exclude(id = contact_id):
# 		print('exists')
# 		return True
# 	else:
# 		return False
	


