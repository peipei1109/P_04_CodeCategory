#-*-coding:UTF-8 -*-
import matplotlib.pyplot as plt
#函数也是对象，可以有自己的属性哦~~~
#定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

#绘制带箭头的注释
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

#测试是否能够正确的画树   
# def createPlot():
   # fig = plt.figure(1, facecolor='white')
   # fig.clf()
   # createPlot.ax1 是一个全局变量
   # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses 
   # plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
   # plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
   # plt.show()  

#下面这个函数没生效，奇怪得不行   
# def createPlot():
    
    # fig=plt.figure(1,facecolor='white')
    # fig.clf() #单独注释这一行也没发现加上边框，这个不知道什么原因~~以后瞅瞅
    # createPlot.ax1=plt.subplot(111,frameon=False)
    # plotNode=('aaa',(0.5,0.1),(0.1,0.5),decisionNode)
    # plotNode=('wwww',(0.8,0.1),(0.3,0.8),leafNode)
    # plt.show()
    
    
def getNumLeafs(myTree):
    numLeafs=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs +=1
    return numLeafs

def getTreeDepth(myTree):
    maxDepth=0
    global thisDepth   #加一个全局关键字吧。。
    # thisDepth =1  用这一句代替上面那一句也可以，我也不知道为什么
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    
    for key in secondDict.keys():
    #测试节点数据类型是否为字典
        if type(secondDict[key]).__name__=='dict':
            thisDepth += getTreeDepth(secondDict[key])
        else:
            thisDepth =1
        if thisDepth>maxDepth:
            maxDepth=thisDepth
    return maxDepth
    
    
#为了测试 getNumLeafs和  getTreeDepth
 
def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i] 

#在父子节点间填充文本信息
def plotMidText(cnTrPt,parentPt,txtString):
    xMid=(parentPt[0]-cnTrPt[0])/2.0+cnTrPt[0]
    yMid=(parentPt[1]-cnTrPt[1])/2.0+cnTrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString,va="center", ha="center",rotation=30) #添加的文字旋转30度
    
#这个还不太懂啊~   
def plotTree(myTree,parentPt,nodeTxt):
    #计算宽与高
    numLeafs=getNumLeafs(myTree)
    depth=getTreeDepth(myTree)
    firstStr=myTree.keys()[0]
    print 'y:',plotTree.y0ff,"x:",plotTree.x0ff,"numLeafs:",numLeafs
    #计算树/子树的根的坐标~~~~
    cnTrPt=(plotTree.x0ff+(1.0+float(numLeafs))/2.0/plotTree.totalW,plotTree.y0ff) #明白了~~haha 
    print  cnTrPt
    #标记子节点属性值
    plotMidText(cnTrPt,parentPt,nodeTxt)
    plotNode(firstStr,cnTrPt,parentPt,decisionNode)
    secondDict=myTree[firstStr]
    #减少Y偏移
    plotTree.y0ff=plotTree.y0ff-1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cnTrPt,str(key))
        else:
            plotTree.x0ff=plotTree.x0ff+1.0/plotTree.totalW
            print plotTree.x0ff
            plotNode(secondDict[key],(plotTree.x0ff,plotTree.y0ff),cnTrPt,leafNode)
            plotMidText((plotTree.x0ff,plotTree.y0ff),cnTrPt,str(key))
    #这句话不知道干嘛的，后来好像是明白了，因为画完其子树后回到根节点高度~~
    plotTree.y0ff=plotTree.y0ff+1.0/plotTree.totalD
 
            
def createPlot(inTree):
    fig=plt.figure(1, facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111 , frameon=False, **axprops)
    plotTree.totalW=float(getNumLeafs(inTree))
    plotTree.totalD=float(getTreeDepth(inTree))
    plotTree.x0ff=-0.5/plotTree.totalW
    print plotTree.x0ff
    plotTree.y0ff=1.0
    plotTree(inTree,(0.5,1.0),'')
    plt.show()
    
    
 
if __name__=='__main__':
    # createPlot()
    myTree=retrieveTree(1)
    print getTreeDepth(myTree)
    print getNumLeafs(myTree)
    createPlot(myTree)
    
    