from django.shortcuts import render, redirect
import random
from hhs.models import home as hin
from hhs.models import rooms as rin
from hhs.models import sofa as sin
from hhs.models import kitchen as kin
from hhs.models import bathroom as brin
from hhs.models import toilet as trin
from hhs.models import carpet as cin
from hhs.models import car as carin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages 
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')
def home(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            troom = request.POST.get('troom')
            tbal = request.POST.get('tbal')
            tchimney = request.POST.get('tchimney')
            tsofa = request.POST.get('tsofa')
            tcarpet = request.POST.get('tcarpet')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            homein = hin(username = username, fullname = fname, email = email, troom = troom, tbal = tbal, tchimney = tchimney, tsofa = tsofa, tcarpet = tcarpet, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            homein.save()
            subject = f'Order Received For HRM Services For House Cleaning'
            message = f'''
Dear HRM Team,
An Order Of House Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Rooms In House: {troom}
Total Balcony: {tbal}
Total Chimney: {tchimney}
Total Seats On Sofa: {tsofa}
Total Carpet In House: {tcarpet}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For House Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Rooms In House: {troom}
Total Balcony: {tbal}
Total Chimney: {tchimney}
Total Seats On Sofa: {tsofa}
Total Carpet In House: {tcarpet}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/home')
            
        return render(request, 'home.html')
def rooms(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            tfans = request.POST.get('tfans')
            talmirah = request.POST.get('talmirah')
            tflooring = request.POST.get('tflooring')
            tarea = request.POST.get('tarea')
            tcarpet = request.POST.get('tcarpet')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            roomin = rin(username = username, fullname = fname, email = email, tfans = tfans, talmirah = talmirah, tflooring = tflooring, tarea = tarea, tcarpet = tcarpet, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            roomin.save()
            subject = f'Order Received For HRM Services For Room Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Room Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Fans In Rooms: {tfans}
Total Almirah: {talmirah}
Type Of Flooring: {tflooring}
Total Area Of Room: {tarea}
Total Carpet In House: {tcarpet}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Room Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Fans In Rooms: {tfans}
Total Almirah: {talmirah}
Type Of Flooring: {tflooring}
Total Area Of Room: {tarea}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/rooms')
        return render(request, 'rooms.html')
def sofa(request):
    
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            tseats = request.POST.get('tseats')
            tsofa = request.POST.get('tsofa')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            sofain = sin(username = username, fullname = fname, email = email, tseats = tseats, tsofa = tsofa, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            sofain.save()
            subject = f'Order Received For HRM Services For Sofa Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Sofa Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Seats On Sofa: {tsofa}
Type Of Sofa: {tsofa}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Sofa Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Seats On Sofa: {tseats}
Type Of Sofa: {tsofa}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/sofa')
        return render(request, 'sofa.html')
def kitchen(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            tcupboard = request.POST.get('tcupboard')
            tchimney = request.POST.get('tchimney')
            tfridge = request.POST.get('tfridge')
            tro = request.POST.get('tro')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            kitchenin = kin(username = username, fullname = fname, email = email, tcupboard = tcupboard, tchimney = tchimney, tfridge = tfridge, tro = tro, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            kitchenin.save()
            subject = f'Order Received For HRM Services For Kitchen Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Kitchen Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Cupboards In Kitchen: {tcupboard}
Total Chimney In Kitchen: {tchimney}
Total Fridge In Kitchen: {tfridge}
Total RO In Kitchen: {tro}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Kitchen Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Cupboards In Kitchen: {tcupboard}
Total Chimney In Kitchen: {tchimney}
Total Fridge In Kitchen: {tfridge}
Total RO In Kitchen: {tro}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/kitchen')
        return render(request, 'kitchen.html')
def bathroom(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            tglass = request.POST.get('tglass')
            tbuckets = request.POST.get('tbuckets')
            ttubs = request.POST.get('ttubs')
            ttaps = request.POST.get('ttaps')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            brinin = brin(username = username, fullname = fname, email = email, tglass = tglass, tbuckets = tbuckets, ttubs = ttubs, ttaps = ttaps, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            brinin.save()
            subject = f'Order Received For HRM Services For Bathroom Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Bathroom Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Glass In Bathroom: {tglass}
Total Buckets: {tbuckets}
Total Tubs: {ttubs}
Total Taps: {ttaps}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Bathroom Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Glass In Bathroom: {tglass}
Total Buckets: {tbuckets}
Total Tubs: {ttubs}
Total Taps: {ttaps}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/bathroom')
        return render(request, 'bathroom.html')
def toilet(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            tglass = request.POST.get('tglass')
            ttaps = request.POST.get('ttaps')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            trinin = trin(username = username, fullname = fname, email = email, tglass = tglass, ttaps = ttaps, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            trinin.save()
            subject = f'Order Received For HRM Services For Toilet Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Toilet Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Glass In Bathroom: {tglass}
Total Taps: {ttaps}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Toilet Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Total Glass In Bathroom: {tglass}
Total Taps: {ttaps}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/toilet')
        return render(request, 'toilet.html')
def carpet(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            lcarpet = request.POST.get('lcarpet')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            ciin = cin(username = username, fullname = fname, email = email, lcarpet = lcarpet, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            ciin.save()
            subject = f'Order Received For HRM Services For Carpet Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Carpet Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Dimensions Of Carpet: {lcarpet}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Carpet Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Dimensions Of Carpet: {lcarpet}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/carpet')
        return render(request, 'carpet.html')
def car(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            ncar = request.POST.get('ncar')
            wcar = request.POST.get('wcar')
            tcar = request.POST.get('tcar')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            ph1 = request.POST.get('ph1')
            ph2 = request.POST.get('ph2')
            otser = request.POST.get('otser')
            cariin = carin(username = username, fullname = fname, email = email, ncar = ncar, wcar = wcar, tcar = tcar, pincode = pincode, address = address, ph1 = ph1, ph2 = ph2, otser = otser)
            cariin.save()
            subject = f'Order Received For HRM Services For Car Cleaning'
            message = f'''
Dear HRM Team,
An Order Of Car Cleaning Service Is Received Please Process It Urgently
Here Are Some Details About {fname}:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Name Of Car: {ncar}
Wheels Of Car: {wcar}
Type Of Car: {tcar}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 
Any Other Service Needed: {otser} 
Thanks And Regards
{fname}, Valuable Costumer
HRM Services'''
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = ['ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            subjectq = f'Order Placed For HRM Services For Car Cleaning'
            messageq = f'''
Dear {fname},
Your Order Has Been Placed, Our Representative Will Contact You Urgently
Here Are Some Details Your Entered:
Username: {username}
Full Name: {fname}
E-Mail: {email}
Name Of Car: {ncar}
Wheels Of Car: {wcar}
Type Of Car: {tcar}
Pincode: {pincode}
Address: {address}
Phone Number 1: {ph1}
Phone Number 2: {ph2} 

Any Other Service Needed: {otser} 

Thanks And Regards
HRM Team
Contact Us:
Phone Number: 1234567890
Mail Id: kwswhwmw@gmail.com
Shop Number: 786
Shopping Arcade
Mahagun Mall
Noida Extention
Kisan Chauk'''
            recipient_listq = [email, 'ritkumar37@gmail.com', 'mann4960@gmail.com', 'skh930@gmail.com', 'swkwhw@gmail.com', 'kwswhwmw@gmail.com'] 
            send_mail(subjectq, messageq, email_from, recipient_listq)
            messages.success(request, 'Your Order Has Been Placed, Our Representative Will Contact You Shortly & Get More Update On Your Mail Id')
            return redirect('/car')
        return render(request, 'car.html')
def login(request):
    if request.method == "POST":
        name = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect('/')
    return render(request, 'login.html')
def logout(request):
    auth_logout(request)
    return redirect('login')
def signup(request):
    if request.method == "POST":
        name = random.randint(10000000, 1000000000000)
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if User.objects.filter(email = email).exists():
            return redirect('/mailerror')
        user = User.objects.create_user(name, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        subject = 'Here Is Your Username And Password For Login In HRM Services'
        message = f'''Hi {fname} {lname}, Thank You For Registering In HRM Services
Here Is Your Username For Login: {name} 
And Password Also: {password}
Do Not Share These Credentials With Anyone
Thanks And Regards
Krishna Wadhwani
HRM Services'''
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email] 
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/know')
    return render(request, 'signup.html')
def know(request):
    return render(request, 'know.html')
def mailerror(request):
    return render(request, 'mailerror.html')