import datetime as dt

#  TIC TAC TOE UTILS
def process_matrix(xoro,sofar,next_move):
    matrix=[    [{"id": "0-0", "v": "X"},
                 {"id": "0-1", "v": "-"},
                 {"id": "0-2", "v": "-"},
                ],
                [{"id": "1-0", "v": "O"},
                 {"id": "1-1", "v": "-"},
                 {"id": "1-2", "v": "-"},
                ],
                [{"id": "2-0", "v": "-"},
                 {"id": "2-1", "v": "-"},
                 {"id": "2-2", "v": "-"},
                ],                
            ]
    matrix=list([])
    rowct=3
    colct=3
    cellctr=0
    for r in range(rowct):
        newrow=list([])
        for c in range(colct):
            nextval = sofar[cellctr]
            newcell=dict({"id": str(r)+"-"+str(c), "v": nextval })
            cellctr=cellctr+1
            newrow.append(newcell)
        matrix.append(newrow)
    #print(matrix)
    
    if next_move:
        sofar=""
        try:
            next_row=int(next_move.split("-")[0])
            next_col=int(next_move.split("-")[1])
            rc=0
            new_matrix=list([])
            for row in matrix:
                new_row=list([])
                if rc==next_row:
                    c=0
                    for col in row:
                        new_cell=dict({})
                        new_cell["id"]=col["id"]
                        if c== next_col:
                            #new_cell.id=str(rc)+"-"+str(c)
                            new_cell["v"]=xoro                      
                        else:
                            new_cell["v"]=col["v"]
                        sofar=sofar+new_cell["v"]
                        new_row.append(new_cell)
                        c=c+1 
                else:
                    for col in row:
                        new_cell=dict({})
                        new_cell["id"]=col["id"]
                        new_cell["v"]=col["v"]
                        sofar=sofar+new_cell["v"]
                        new_row.append(new_cell)
                rc=rc+1
                new_matrix.append(new_row)
            #print(new_matrix)
            matrix=new_matrix
            #print(matrix[next_row][next_col])
            #matrix[next_row][next_col].v=xoro 
        except:
            pass

    return matrix, sofar

def check_game_status(matrix):
    gameover=False 
    # Check Row Win
    for row in matrix:
        gameover_by_row=True
        prev_cell=None
        if gameover==False:
            for cell in row:
                if prev_cell:
                    if cell["v"] not in ["X","O"]:
                        gameover_by_row=False 
                    elif cell["v"] != prev_cell:
                        gameover_by_row=False
                prev_cell=cell["v"]
            if gameover_by_row==True:
                gameover=True 

    # Check Vertical WIN
    if gameover==False:
        cellctr=0
        for col in matrix[0]:
            if gameover==False:
                gameover_by_cell=True
                root_cell=col["v"]
                for row in matrix:
                    if row[cellctr]["v"] != root_cell:
                        gameover_by_cell=False  
                if gameover_by_cell==True and root_cell in ["X","O"]:
                    gameover=True 
            cellctr = cellctr+1

    # CHECK DIAGONAL
    if gameover==False:
        cellctr=0
        root_cell=matrix[0][0]["v"]
        gameover_by_cell=True
        for row in matrix:
            if row[cellctr]["v"] != root_cell:
                gameover_by_cell=False
            cellctr=cellctr+1
        if gameover_by_cell==True and root_cell in ["X","O"]:
            gameover=True
       
    # CHECK REVERSE DIAGONAL
    if gameover==False:
        cellctr=len(matrix[0])-1
        root_cell=matrix[0][cellctr]["v"]
        gameover_by_cell=True
        for row in matrix:
            if row[cellctr]["v"] != root_cell:
                gameover_by_cell=False
            cellctr=cellctr-1
        if gameover_by_cell==True and root_cell in ["X","O"]:
            gameover=True
    
    return gameover


#BLACK JACK UTILS

def pickone(mylist,random_num=None):
    """
        Pass in a list of items, it will pick an index at random
    """
    x=0
    while x<99999:
        x+=1
    if random_num:
        return ((random_num*random_num)+dt.datetime.now().day+dt.datetime.now().second+dt.datetime.now().hour+dt.datetime.now().microsecond)%len(mylist)
    else:
        return (dt.datetime.now().day+dt.datetime.now().second+dt.datetime.now().hour+dt.datetime.now().microsecond)%len(mylist)
    
def pickacard():
    random_num=65
    cardnums=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    vals=['2','3','4','5','6','7','8','9','10','10','10','10','10']
    suits=['Diamonds','Spades','Hearts','Clubs']
    card_index=pickone(cardnums,random_num)
    val=vals[card_index]
    face=cardnums[card_index]
    suit=suits[pickone(suits,random_num)]
    
    return face+","+suit+","+val

def getdealerhand(dh,next_move):
    dealerhand = []
    score=0
    ctr=0
    dh_arr=list([])

    if len(dh)>0:
        for nextitem in dh.split("|"):
            face=nextitem.split(",")[0]
            suit=nextitem.split(",")[1]
            val=nextitem.split(",")[2]
            score=score+int(val)
            hidden=True 
            if next_move:
                if next_move in ("stay","hold"):
                    hidden=False 
            if ctr>0:
                hidden=False 
            ctr+=1
            dealerhand.append({"face":face,"suit": suit,"hidden": hidden })
            dh_arr.append(face+","+suit+","+val)
    while len(dealerhand) < 2:
        nextitem=pickacard()
        face=nextitem.split(",")[0]
        suit=nextitem.split(",")[1]
        val=nextitem.split(",")[2]
        score=score+int(val)
        hidden=True 
        if next_move:
            if next_move in ("stay","hold"):
                hidden=False 
        if ctr>0:
            hidden=False 
        ctr+=1
        dealerhand.append({"face":face,"suit": suit,"hidden": hidden })
        dh_arr.append(face+","+suit+","+val)

    if next_move in ("stay","hold"):
        while score <= 17:
            nextitem=pickacard()
            face=nextitem.split(",")[0]
            suit=nextitem.split(",")[1]
            val=nextitem.split(",")[2]
            #score=score+int(val)
            dealerhand.append({"face":face,"suit": suit,"hidden": False })
            dh_arr.append(face+","+suit+","+val)
            score= evaluatescore("|".join(dh_arr))
            print("|".join(dh_arr))
            print(score)
    dh = "|".join(dh_arr)

    return dealerhand,dh,score 
        

def getplayerhand(ph,next_move):
    playerhand = []
    score=0
    ctr=0
    ph_arr=list([])

    if len(ph)>0:
        for nextitem in ph.split("|"):
            face=nextitem.split(",")[0]
            suit=nextitem.split(",")[1]
            val=nextitem.split(",")[2]
            score=score+int(val)
            ctr+=1
            playerhand.append({"face":face,"suit": suit })
            ph_arr.append(face+","+suit+","+val)
    while len(playerhand) < 2:
        nextitem=pickacard()
        face=nextitem.split(",")[0]
        suit=nextitem.split(",")[1]
        val=nextitem.split(",")[2]
        score=score+int(val)
        hidden=True 
        if next_move:
            if next_move in ("stay","hold"):
                hidden=False 
        if ctr>0:
            hidden=False 
        ctr+=1
        playerhand.append({"face":face,"suit": suit })
        ph_arr.append(face+","+suit+","+val)

    if next_move in ("anothercard"):
        nextitem=pickacard()
        face=nextitem.split(",")[0]
        suit=nextitem.split(",")[1]
        val=nextitem.split(",")[2]
        score=score+int(val)
        playerhand.append({"face":face,"suit": suit })
        ph_arr.append(face+","+suit+","+val)
    ph = "|".join(ph_arr)

    return playerhand,ph,score 

def evaluatescore(hand):
    scores=list([])
    for card in hand.split("|"):
        face=card.split(",")[0]
        val=card.split(",")[2]
        if scores==[]:
            if face in ("A","Ace"):
                scores.append(1)
                scores.append(10)
            else:    
                scores.append(int(val))
        else:
            temp=list([])
            for score in scores:
                temp.append(score)
            scores=list([])
            if face in ("A","Ace"):
                for score in temp:
                    scores.append(score+1)
                    scores.append(score+10)
            else:
                for score in temp:
                    scores.append(score+int(val))
    max_score=-1
    max_score_without_bust=-1
    for score in scores:
        if max_score_without_bust<score and score <=21:
            max_score_without_bust=score 
        if max_score < score:
            max_score=score 
    if max_score_without_bust==-1 and max_score> 0:
        return max_score
    if max_score_without_bust< 21 and max_score==21:
        return 21

    return max_score_without_bust
        

                

