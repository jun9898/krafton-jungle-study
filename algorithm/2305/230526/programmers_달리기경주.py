def solution(players, callings):
    playerDic = {player:i+1 for i,player in enumerate(players)}
    indexPlayer = {i+1:player for i,player in enumerate(players)}
    for i in callings:
        a = playerDic[i]
        b = indexPlayer[a-1]
        
        playerDic[b] = a
        playerDic[i] = a-1
        
        indexPlayer[a] = b 
        indexPlayer[a-1] = i   

    return list(indexPlayer.values())