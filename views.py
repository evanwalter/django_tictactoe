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
