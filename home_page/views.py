import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from home_page.again import again
from home_page.models import Yysinfor, YysSmallInfor, Change, Headgame, SmallTitle, Headbranch, My_img, Gamedirectory,JumpHtm


def head_infor(request):
    result = {}
    try:
        li = []
        if request.method == 'GET':
            yysinfor = Yysinfor.objects.all()
            for yys in yysinfor:
                yys.infor = Change.qs_to_dict(YysSmallInfor.objects.filter(uid=yys.id))
                li.append(yys.to_dict())
            result.update(static=200, msg='success', data=li)
        return HttpResponse(json.dumps(result), content_type='Application/json')
    except Exception as a:
        result.update(static=404, msg='GG')
        return HttpResponse(json.dumps(result))


def catalog(request):
    li = []
    result = {}
    try:
        headgames = Headgame.objects.all()
        for headgame in headgames:
            subs = headgame.headbranch_set.all()
            # headgame.smalltitle = Change.qs_to_dict(Headbranch.objects.filter(mid=headgame.id))
            # headgame.smalltitle = Change.qs_to_dict(subs)
            # li.append(headgame.to_dict())
            for sub in subs:
                infors = sub.smalltitle_set.all()
                pagegame = sub.pagegame.all()
                # sub.pagegames = Change.qs_to_dict(sub.pagegame.all())
                # sub.title = Change.qs_to_dict(sub.smalltitle_set.filter())
                # headgame.smalltitle = Change.qs_to_dict(subs)
                # li.append(headgame.to_dict())
                for infor in infors:
                    games = infor.game.all()
                    # infor.games = infor.qs_to_dict(infor.game.all())
                    for game in games:
                        game.img = Change.qs_to_dict(game.my_img_set.all())
                    infor.imggame = Change.qs_to_dict(games)
                sub.inforgame = Change.qs_to_dict(infors)
                sub.pagegames = Change.qs_to_dict(pagegame)
            headgame.smalltitle = Change.qs_to_dict(subs)
            li.append(headgame.to_dict())
            #         # a = infor.game.all()
            #         # s = infor.qs_to_dict(a)  #bug原因    infor.game 与 infor.game.all() 的game相同
            #         # infor.game = infor.qs_to_dict(a)
            #         infor.games = Change.qs_to_dict(infor.game.all())
            #         li.append(infor.to_dict())
        result.update(static=200, msg='success', data=li)
        return HttpResponse(json.dumps(result), content_type='Application/json')
    except Exception as e:
        return HttpResponse(e)


def search(request):
    # try:
    li = []
    context={}
    result = {}
    if request.method == 'GET':
        name = request.GET.get('key')
        gameinfo = Gamedirectory.objects.filter(game_name__contains=name)
        if gameinfo:
            for game in gameinfo:
                li.append(game.to_dict())
            context = {'li':li}
            result.update(static=200, msg='success', data=li)
            # return render(request,'search.html',context=context)
    # return render(request,'item_infor.html')
    # except:
    #     return HttpResponse('hh')
    return HttpResponse(json.dumps(result), content_type='Application/json')
    # return render(request, 'search.html', context=context)


def info(request):
    result = {}
    li = []
    if request.method == 'GET':
        name = request.GET.get('key')
        games = Gamedirectory.objects.filter(game_name__contains=name)
        if games:
            for game in games:
                li.append(game.to_dict())
            result.update(state=200,msg='success',data=li)
        return HttpResponse(json.dumps(result),content_type='Application/json')

def jump_htm(request):
    result = {}
    li = []
    if request.method == 'GET':
        gname = request.GET.get('gname')
        games = Gamedirectory.objects.filter(game_name=gname)
        if games:
            for game in games:
                sub = game.jumphtm_set.all()
                game.info = Change.qs_to_dict(sub)
                li.append(game.to_dict())
            result.update(status=200,msg='success',data=li)
    return HttpResponse(json.dumps(result),'Application/json')


def shiyan(request):
    li = [{'static':200,'msg':'success','data':['a',5]}]
    a = {'shiyan':li}
    return render(request,'shiyan.html',context=a)
