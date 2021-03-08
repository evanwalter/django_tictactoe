from django.http import HttpResponse
from django.shortcuts import render
from .utils import *


def index(request,next_move=None):
   
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')
    
def game(request):
    next_move=request.GET.get("next_move",None)
    xoro=request.GET.get("xoro","O")
    sofar=request.GET.get("sofar","----------")

    #matrix=[["X","-","-"],["-","O","-"],["-","-","-"]]

    matrix, sofar = process_matrix(xoro,sofar,next_move)

    if xoro=="X":
        xoro="O"
    else:
        xoro="X"

    game_status=check_game_status(matrix)    
    
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'game.html', {'matrix': matrix,"xoro": xoro,
                                            "sofar": sofar,
                                            "game_status": game_status})

def blackjack(request):
    next_move=request.GET.get("next_move","another_card")
    xoro=request.GET.get("xoro","O")
    sofar=request.GET.get("sofar","----------")
    game_over = False
    show_dealer_score=False 

    dh= request.GET.get("dh","")
    ph= request.GET.get("ph","")
    
    playerhand,ph,playerscore=getplayerhand(ph,next_move)
    if playerscore>21:
        game_over=True 

    dealerhand,dh,dealerscore=getdealerhand(dh,next_move)
    if next_move=="hold":
        game_over=True 
    
    game_status=""
    if playerscore > 21:
        game_status="BUST!!!"
    elif dealerscore > 21:
        game_status="Dealer Bust!  You won!"
        show_dealer_score=True 
    elif game_over and dealerscore== playerscore:
        game_status="Scratch!"
        show_dealer_score=True
    elif game_over and playerscore>dealerscore:
        game_status="You won!"
        show_dealer_score=True 
    elif game_over and dealerscore> playerscore:
        game_status="You lost."
        show_dealer_score=True 

    return render(request, 'blackjack.html', {"xoro": xoro,
                                            "sofar": sofar,
                                            "dh": dh,"ph": ph,
                                            "playerhand": playerhand,"playerscore": playerscore,
                                            "dealerhand": dealerhand,"dealerscore": dealerscore,
                                            "show_dealer_score": show_dealer_score,
                                            "game_over": game_over,"game_status": game_status})
