from flask import Blueprint, request
 
ag1_40323107_cdw14 = Blueprint('ag1_40323107_cdw14', __name__, url_prefix='/ag1_40323107_cdw14', template_folder='templates')
 
head_str = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
 
</head>
<body>
 
<script>
window.onload=function(){
brython(1);
}
</script>
 
<canvas id="plotarea" width="800" height="800"></canvas>
'''
 
tail_str = '''
</script>
</body>
</html>
'''
 
chain_str = '''
<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-250, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  
 
# 將繪製鏈條輪廓的內容寫成 class 物件
class chain():
    # 輪廓的外型設為 class variable
    chamber = "M -6.8397, -1.4894 \
            A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
            A 40, 40, 0, 0, 1, 6.8397, -18.511 \
            A 7, 7, 0, 1, 0, -6.8397, -18.511 \
            A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    #chamber = "M 0, 0 L 0, -20 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    def __init__(self, fillcolor="green", border=True, strokecolor= "tan", linewidth=2, scale=1):
        self.fillcolor = fillcolor
        self.border = border
        self.strokecolor = strokecolor
        self.linewidth = linewidth
        self.scale = scale
 
    # 利用鏈條起點與終點定義繪圖
    def basic(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, self.scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, v=False):
        # 若 v 為 True 則為虛擬 chain, 不 render
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.v = v
        # 注意, cgoChamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole0 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)*self.scale
        y2 = y1 + 20*math.sin(rot*deg)*self.scale
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        if v == False:
            cgo.render(basic1, x1, y1, self.scale, 0)
 
        return x2, y2
'''
 
@ag1_40323107_cdw14.route('/gear0')
def gear0():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear0</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear1' width='800' height='750'></canvas>
 
<script type="text/python">
# 將 導入的 document 設為 doc 主要原因在於與舊程式碼相容
from browser import document as doc
# 由於 Python3 與 Javascript 程式碼已經不再混用, 因此來自 Javascript 的變數, 必須居中透過 window 物件轉換
from browser import window
# 針對 Javascript 既有的物件, 則必須透過 JSConstructor 轉換
from javascript import JSConstructor
import math
 
# 主要用來取得畫布大小
canvas = doc["gear1"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
# 針對類別的轉換, 將 Cango.js 中的 Cango 物件轉為 Python cango 物件
cango = JSConstructor(window.Cango)
# 針對變數的轉換, shapeDefs 在 Cango 中資料型別為變數, 可以透過 window 轉換
shapedefs = window.shapeDefs
# 目前 Cango 結合 Animation 在 Brython 尚無法運作, 此刻只能繪製靜態圖形
# in CangoAnimation.js
#interpolate1 = window.interpolate
# Cobi 與 createGearTooth 都是 Cango Javascript 程式庫中的物件
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="plotarea" 的 canvas 上
cgo = cango("gear1")
 
######################################
# 畫正齒輪輪廓
#####################################
# n 為齒數
n = 17
# pa 為壓力角
pa = 25
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
# Module = mm of pitch diameter per tooth
m = 0.8*canvas.width/n
# pr 為節圓半徑
pr = n*m/2 # gear Pitch radius
# generate gear
data = creategeartooth(m, n, pa)
# Brython 程式中的 print 會將資料印在 Browser 的 console 區
#print(data)
gearTooth = cobj(data, "SHAPE", {
        "fillColor":"#ddd0dd",
        "border": True,
        "strokeColor": "#606060" })
gearTooth.rotate(180/n) # rotate gear 1/2 tooth to mesh
# 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
gear = gearTooth.dup()
# gear 為單一齒的輪廓資料
#cgo.render(gearTooth)
 
# 利用單齒輪廓旋轉, 產生整個正齒輪外形
for i in range(1, n):
    # 將 gearTooth 中的資料複製到 newTooth
    newTooth = gearTooth.dup()
    # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
    newTooth.rotate(360*i/n)
    # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
    gear.appendPath(newTooth, True) # trim move command = True
 
# 建立軸孔
# add axle hole, hr 為 hole radius
hr = 0.6*pr # diameter of gear shaft
shaft = cobj(shapedefs.circle(hr), "PATH")
shaft.revWinding()
gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
cx = canvas.width/2
cy = canvas.height/2
gear.translate(cx, cy)
# render 繪出靜態正齒輪輪廓
cgo.render(gear)
</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/gear1')
def gear1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear1</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear1' width='800' height='750'></canvas>
 
<script type="text/python">
# 將 導入的 document 設為 doc 主要原因在於與舊程式碼相容
from browser import document as doc
# 由於 Python3 與 Javascript 程式碼已經不再混用, 因此來自 Javascript 的變數, 必須居中透過 window 物件轉換
from browser import window
# 針對 Javascript 既有的物件, 則必須透過 JSConstructor 轉換
from javascript import JSConstructor
import math
 
# 主要用來取得畫布大小
canvas = doc["gear1"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
# 針對類別的轉換, 將 Cango.js 中的 Cango 物件轉為 Python cango 物件
cango = JSConstructor(window.Cango)
# 針對變數的轉換, shapeDefs 在 Cango 中資料型別為變數, 可以透過 window 轉換
shapedefs = window.shapeDefs
# 目前 Cango 結合 Animation 在 Brython 尚無法運作, 此刻只能繪製靜態圖形
# in CangoAnimation.js
#interpolate1 = window.interpolate
# Cobi 與 createGearTooth 都是 Cango Javascript 程式庫中的物件
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="plotarea" 的 canvas 上
cgo = cango("gear1")
 
######################################
# 畫正齒輪輪廓
#####################################
# n 為齒數
n = 20
# pa 為壓力角
pa = 25
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
# Module = mm of pitch diameter per tooth
m = 0.5*canvas.width/n
# pr 為節圓半徑
pr = n*m/2 # gear Pitch radius
# generate gear
data = creategeartooth(m, n, pa)
# Brython 程式中的 print 會將資料印在 Browser 的 console 區
#print(data)
gearTooth = cobj(data, "SHAPE", {
        "fillColor":"#ddd0dd",
        "border": True,
        "strokeColor": "#606060" })
gearTooth.rotate(180/n) # rotate gear 1/2 tooth to mesh
# 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
gear = gearTooth.dup()
# gear 為單一齒的輪廓資料
#cgo.render(gearTooth)
 
# 利用單齒輪廓旋轉, 產生整個正齒輪外形
for i in range(1, n):
    # 將 gearTooth 中的資料複製到 newTooth
    newTooth = gearTooth.dup()
    # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
    newTooth.rotate(360*i/n)
    # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
    gear.appendPath(newTooth, True) # trim move command = True
 
# 建立軸孔
# add axle hole, hr 為 hole radius
hr = 0.4*pr # diameter of gear shaft
shaft = cobj(shapedefs.circle(hr), "PATH")
shaft.revWinding()
gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
cx = canvas.width/2
cy = canvas.height/2
gear.translate(cx, cy)
# render 繪出靜態正齒輪輪廓
cgo.render(gear)
deg=math.pi/180
Line=cobj(['M',cx,cy,'L',
    cx+pr*math.cos(1620/n*deg),
    cy+pr*math.sin(1620/n*deg)],"PATH",{
     'strokeColor':'blue','linewidth':5})
cgo.render(Line)
Line2=cobj(['M',cx,cy,'L',
    cx+pr*math.cos(180),
    cy+pr*math.sin(0)],"PATH",{
     'strokeColor':'red','linewidth':5})
cgo.render(Line2)

</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/gear2')
def gear2():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear2</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>


<canvas id='gear2' width='800' height='700'></canvas>
 
<script type="text/python3">
# 導入 browser 模組中的 document, 並設為 doc 變數
from browser import document as doc
import math
# deg 為角度轉為徑度的轉換因子
deg = math.pi/180.
# 定義 Spur 類別
class Spur(object):
    def __init__(self, ctx):
        self.ctx = ctx
 
    def create_line(self, x1, y1, x2, y2, width=3, fill="red"):
        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.moveTo(x1, y1)
        self.ctx.lineTo(x2, y2)
        self.ctx.strokeStyle = fill
        self.ctx.stroke()
    #
    # 定義一個繪正齒輪的繪圖函式
    # midx 為齒輪圓心 x 座標
    # midy 為齒輪圓心 y 座標
    # rp 為節圓半徑, n 為齒數
    # pa 為壓力角 (deg)
    # rot 為旋轉角 (deg)
    # 已經針對 n 大於等於 52 齒時的繪圖錯誤修正, 因為 base circle 與齒根圓大小必須進行判斷
    def Gear(self, midx, midy, rp, n=20, pa=20, color="black"):
        # 齒輪漸開線分成 15 線段繪製
        imax = 15
        # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
        self.create_line(midx, midy, midx, midy-rp)
        # 畫出 rp 圓, 畫圓函式尚未定義
        #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
        # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
        # 模數也就是齒冠大小
        a=2*rp/n
        # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
        d=2.5*rp/n
        # ra 為齒輪的外圍半徑
        ra=rp+a
        # 畫出 ra 圓, 畫圓函式尚未定義
        #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
        # rb 則為齒輪的基圓半徑
        # 基圓為漸開線長齒之基準圓
        rb=rp*math.cos(pa*deg)
        # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
        #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
        # rd 為齒根圓半徑
        rd=rp-d
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
        #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
        # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
        # 將圓弧分成 imax 段來繪製漸開線
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        if rd>rb:
            dr = (ra-rd)/imax
        else:
            dr=(ra-rb)/imax
        # tan(pa*deg)-pa*deg 為漸開線函數
        sigma=math.pi/(2*n)+math.tan(pa*deg)-pa*deg
        for j in range(n):
            ang=-2.*j*math.pi/n+sigma
            ang2=2.*j*math.pi/n+sigma
            lxd=midx+rd*math.sin(ang2-2.*math.pi/n)
            lyd=midy-rd*math.cos(ang2-2.*math.pi/n)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(alpha-ang)
                ypt=r*math.cos(alpha-ang)
                xd=rd*math.sin(-ang)
                yd=rd*math.cos(-ang)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    lfx=midx+xpt
                    lfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # the line from last end of dedendum point to the recent
            # end of dedendum point
            # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
            # 下列為齒根圓上用來近似圓弧的直線
            self.create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=color)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(ang2-alpha)
                ypt=r*math.cos(ang2-alpha)
                xd=rd*math.sin(ang2)
                yd=rd*math.cos(ang2)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    rfx=midx+xpt
                    rfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
            # 下列為齒頂圓上用來近似圓弧的直線
            self.create_line(lfx,lfy,rfx,rfy,fill=color)
 
# 準備在 id="gear2" 的 canvas 中繪圖
canvas = doc["gear2"]
ctx = canvas.getContext("2d")
x = (canvas.width)/2
y = (canvas.height)/2
r = 0.8*(canvas.width/2)
# 齒數
n = 53
# 壓力角
pa = 20
Spur(ctx).Gear(x, y, r, n, pa, "blue")

</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/gear3')
def gear3():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear3</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear3' width='800' height='400'></canvas>
 
<script type="text/python3">
# 導入 browser 模組中的 document, 並設為 doc 變數
from browser import document as doc
import math
# deg 為角度轉為徑度的轉換因子
deg = math.pi/180.
# 定義 Spur 類別
class Spur(object):
    def __init__(self, ctx):
        self.ctx = ctx
 
    def create_line(self, x1, y1, x2, y2, width=3, fill="red"):
        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.moveTo(x1, y1)
        self.ctx.lineTo(x2, y2)
        self.ctx.strokeStyle = fill
        self.ctx.stroke()
    #
    # 定義一個繪正齒輪的繪圖函式
    # midx 為齒輪圓心 x 座標
    # midy 為齒輪圓心 y 座標
    # rp 為節圓半徑, n 為齒數
    # pa 為壓力角 (deg)
    # rot 為旋轉角 (deg)
    # 已經針對 n 大於等於 52 齒時的繪圖錯誤修正, 因為 base circle 與齒根圓大小必須進行判斷
    def Gear(self, midx, midy, rp, n=20, pa=20, color="black"):
        # 齒輪漸開線分成 15 線段繪製
        imax = 15
        # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
        self.create_line(midx, midy, midx, midy-rp)
        # 畫出 rp 圓, 畫圓函式尚未定義
        #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
        # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
        # 模數也就是齒冠大小
        a=2*rp/n
        # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
        d=2.5*rp/n
        # ra 為齒輪的外圍半徑
        ra=rp+a
        # 畫出 ra 圓, 畫圓函式尚未定義
        #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
        # rb 則為齒輪的基圓半徑
        # 基圓為漸開線長齒之基準圓
        rb=rp*math.cos(pa*deg)
        # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
        #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
        # rd 為齒根圓半徑
        rd=rp-d
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
        #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
        # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
        # 將圓弧分成 imax 段來繪製漸開線
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        if rd>rb:
            dr = (ra-rd)/imax
        else:
            dr=(ra-rb)/imax
        # tan(pa*deg)-pa*deg 為漸開線函數
        sigma=math.pi/(2*n)+math.tan(pa*deg)-pa*deg
        for j in range(n):
            ang=-2.*j*math.pi/n+sigma
            ang2=2.*j*math.pi/n+sigma
            lxd=midx+rd*math.sin(ang2-2.*math.pi/n)
            lyd=midy-rd*math.cos(ang2-2.*math.pi/n)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(alpha-ang)
                ypt=r*math.cos(alpha-ang)
                xd=rd*math.sin(-ang)
 
                yd=rd*math.cos(-ang)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    lfx=midx+xpt
                    lfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # the line from last end of dedendum point to the recent
            # end of dedendum point
            # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
            # 下列為齒根圓上用來近似圓弧的直線
            self.create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=color)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(ang2-alpha)
                ypt=r*math.cos(ang2-alpha)
                xd=rd*math.sin(ang2)
                yd=rd*math.cos(ang2)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    rfx=midx+xpt
                    rfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
            # 下列為齒頂圓上用來近似圓弧的直線
            self.create_line(lfx,lfy,rfx,rfy,fill=color)
 
# 準備在 id="gear3" 的 canvas 中繪圖
canvas = doc["gear3"]
ctx = canvas.getContext("2d")
 
# 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
# 壓力角 pa 單位為角度
pa = 20
# 第1齒輪齒數
n_g1 = 17
# 第2齒輪齒數
n_g2 = 11
# 第3齒輪齒數
n_g3 = 13
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
m = (0.8*canvas.width)/(n_g1+n_g2+n_g3)
# 根據模數 m, 計算各齒輪的節圓半徑
rp_g1 = m*n_g1/2
rp_g2 = m*n_g2/2
rp_g3 = m*n_g3/2
#單一正齒輪繪圖呼叫格式 Spur(ctx).Gear(x, y, r, n, pa, "blue")
# 開始繪製囓合齒輪輪廓
# 繪圖第1齒輪的圓心座標, 因為希望繪圖佔去 canvas.width 的 80%, 所以兩邊各預留 10% 距離
x_g1 = canvas.width*0.1+rp_g1
# y 方向繪圖區域上方預留 canvas.height 的 20%
y_g1 = canvas.height*0.2+rp_g1
# 第2齒輪的圓心座標, 假設排列成水平, 表示各齒輪圓心 y 座標相同
x_g2 = x_g1 + rp_g1 + rp_g2
y_g2 = y_g1
# 第3齒輪的圓心座標
x_g3 = x_g1 + rp_g1 + 2*rp_g2 + rp_g3
y_g3 = y_g1
 
# 將第1齒輪順時鐘轉 90 度, 也就是 math.pi/2
# 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
ctx.save()
# translate to the origin of second gear
ctx.translate(x_g1, y_g1)
# rotate to engage
ctx.rotate(math.pi/2)
# put it back
ctx.translate(-x_g1, -y_g1)
# 繪製第一個齒輪輪廓
Spur(ctx).Gear(x_g1, y_g1, rp_g1, n_g1, pa, "blue")
ctx.restore()
 
# 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
ctx.save()
# translate to the origin of second gear
ctx.translate(x_g2, y_g2)
# rotate to engage
ctx.rotate(-math.pi/2-math.pi/n_g2)
# put it back
ctx.translate(-x_g2, -y_g2)
Spur(ctx).Gear(x_g2, y_g2, rp_g2, n_g2, pa, "black")
ctx.restore()
 
# 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
ctx.save()
# translate to the origin of second gear
ctx.translate(x_g3, y_g3)
# rotate to engage
# math.pi+math.pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
# 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
# 第1個 -math.pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
# -math.pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
# (math.pi+math.pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
# 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
# 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
ctx.rotate(-math.pi/2-math.pi/n_g3+(math.pi+math.pi/n_g2)*n_g2/n_g3)
# put it back
ctx.translate(-x_g3, -y_g3)
Spur(ctx).Gear(x_g3, y_g3, rp_g3, n_g3, pa, "red")
ctx.restore()
</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/gear4')
def gear4():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear4</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear1' width='1000' height='900'></canvas>
 
<script type="text/python">
# 將 導入的 document 設為 doc 主要原因在於與舊程式碼相容
from browser import document as doc
# 由於 Python3 與 Javascript 程式碼已經不再混用, 因此來自 Javascript 的變數, 必須居中透過 window 物件轉換
from browser import window
# 針對 Javascript 既有的物件, 則必須透過 JSConstructor 轉換
from javascript import JSConstructor
import math
 
# 主要用來取得畫布大小
canvas = doc["gear1"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
# 針對類別的轉換, 將 Cango.js 中的 Cango 物件轉為 Python cango 物件
cango = JSConstructor(window.Cango)
# 針對變數的轉換, shapeDefs 在 Cango 中資料型別為變數, 可以透過 window 轉換
shapedefs = window.shapeDefs
# 目前 Cango 結合 Animation 在 Brython 尚無法運作, 此刻只能繪製靜態圖形
# in CangoAnimation.js
#interpolate1 = window.interpolate
# Cobi 與 createGearTooth 都是 Cango Javascript 程式庫中的物件
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="plotarea" 的 canvas 上
cgo = cango("gear1")
 
######################################
# 畫正齒輪輪廓
#####################################
def spur(cx,cy,m,n,pa,color,rot):

    # Module = mm of pitch diameter per tooth

    # pr 為節圓半徑
    pr = n*m/2 # gear Pitch radius
    # generate gear
    data = creategeartooth(m, n, pa)
    # Brython 程式中的 print 會將資料印在 Browser 的 console 區
    #print(data)
    gearTooth = cobj(data, "SHAPE", {
            "fillColor":"#ddd0dd",
            "border": True,
            "strokeColor": "#606060" })
    gearTooth.rotate(180/n) # rotate gear 1/2 tooth to mesh
    # 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
    gear = gearTooth.dup()
    # gear 為單一齒的輪廓資料
    #cgo.render(gearTooth)
     
    # 利用單齒輪廓旋轉, 產生整個正齒輪外形
    for i in range(1, n):
        # 將 gearTooth 中的資料複製到 newTooth
        newTooth = gearTooth.dup()
        # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
        newTooth.rotate(360*i/n)
        # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
        gear.appendPath(newTooth, True) # trim move command = True
     
    # 建立軸孔
    # add axle hole, hr 為 hole radius
    hr = 0.6*pr # diameter of gear shaft
    shaft = cobj(shapedefs.circle(hr), "PATH")
    shaft.revWinding()
    gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path

    gear.translate(cx, cy)
    # render 繪出靜態正齒輪輪廓
    cgo.render(gear)
    deg=math.pi/180
    
    Line=cobj(['M',cx,cy,'L',
    cx+pr*math.cos(180/n*deg),
    cy+pr*math.sin(180/n*deg)],"PATH",{
     'strokeColor':color,'linewidth':10})
    cgo.render(Line)

# n 為齒數
n = 15
# pa 為壓力角
pa = 25
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
m = 0.8*canvas.width/n/5
cx = canvas.width/2
cy = canvas.height/2
spur(cx,cy,10,n,pa,'red',0)
spur(cx+150,cy,10,n,pa,'blue',180-180/n)
spur(cx-150,cy,10,n,pa,'green',180-180/n)
spur(cx,cy+150,10,n,pa,'black',170)
spur(cx,cy-150,10,n,pa,'yellow',270-180/n)

</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/gear5')
def gear5():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>gear5</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear2' width='1000' height='1000'></canvas>
 
<script type="text/python3">
# 導入 browser 模組中的 document, 並設為 doc 變數
from browser import document as doc
import math
# deg 為角度轉為徑度的轉換因子
deg = math.pi/180.
# 定義 Spur 類別
class Spur(object):
    def __init__(self, ctx):
        self.ctx = ctx
 
    def create_line(self, x1, y1, x2, y2, width=3, fill="red"):
        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.moveTo(x1, y1)
        self.ctx.lineTo(x2, y2)
        self.ctx.strokeStyle = fill
        self.ctx.stroke()
    #
    # 定義一個繪正齒輪的繪圖函式
    # midx 為齒輪圓心 x 座標
    # midy 為齒輪圓心 y 座標
    # rp 為節圓半徑, n 為齒數
    # pa 為壓力角 (deg)
    # rot 為旋轉角 (deg)
    # 已經針對 n 大於等於 52 齒時的繪圖錯誤修正, 因為 base circle 與齒根圓大小必須進行判斷
    def Gear(self, midx, midy, rp, n=20, pa=20, color="black"):
        # 齒輪漸開線分成 15 線段繪製
        imax = 15
        # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
        self.create_line(midx, midy, midx, midy-rp)
        # 畫出 rp 圓, 畫圓函式尚未定義
        #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
        # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
        # 模數也就是齒冠大小
        a=2*rp/n
        # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
        d=2.5*rp/n
        # ra 為齒輪的外圍半徑
        ra=rp+a
        # 畫出 ra 圓, 畫圓函式尚未定義
        #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
        # rb 則為齒輪的基圓半徑
        # 基圓為漸開線長齒之基準圓
        rb=rp*math.cos(pa*deg)
        # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
        #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
        # rd 為齒根圓半徑
        rd=rp-d
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
        #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
        # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
        # 將圓弧分成 imax 段來繪製漸開線
        # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
        if rd>rb:
            dr = (ra-rd)/imax
        else:
            dr=(ra-rb)/imax
        # tan(pa*deg)-pa*deg 為漸開線函數
        sigma=math.pi/(2*n)+math.tan(pa*deg)-pa*deg
        for j in range(n):
            ang=-2.*j*math.pi/n+sigma
            ang2=2.*j*math.pi/n+sigma
            lxd=midx+rd*math.sin(ang2-2.*math.pi/n)
            lyd=midy-rd*math.cos(ang2-2.*math.pi/n)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(alpha-ang)
                ypt=r*math.cos(alpha-ang)
                xd=rd*math.sin(-ang)
                yd=rd*math.cos(-ang)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    lfx=midx+xpt
                    lfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # the line from last end of dedendum point to the recent
            # end of dedendum point
            # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
            # 下列為齒根圓上用來近似圓弧的直線
            self.create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=color)
            for i in range(imax+1):
                # 當 rd 大於 rb 時, 漸開線並非畫至 rb, 而是 rd
                if rd>rb:
                    r=rd+i*dr
                else:
                    r=rb+i*dr
                theta=math.sqrt((r*r)/(rb*rb)-1.)
                alpha=theta-math.atan(theta)
                xpt=r*math.sin(ang2-alpha)
                ypt=r*math.cos(ang2-alpha)
                xd=rd*math.sin(ang2)
                yd=rd*math.cos(ang2)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                self.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    rfx=midx+xpt
                    rfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
            # 下列為齒頂圓上用來近似圓弧的直線
            self.create_line(lfx,lfy,rfx,rfy,fill=color)
 
# 準備在 id="gear2" 的 canvas 中繪圖
canvas = doc["gear2"]
ctx = canvas.getContext("2d")
x = (canvas.width)/2
y = (canvas.height)/2
r = 0.8*(canvas.width/2)
# 齒數
n = 25
# 壓力角
pa = 20
Spur(ctx).Gear(x, y, r/5, n, pa, "yellow")
Spur(ctx).Gear(x, y+160, r/5, n, pa, "red")
Spur(ctx).Gear(x, y-160, r/5, n, pa, "green")

</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/spur1')
def spur1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>spur</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAxes-1v33.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/flintlockPartDefs-02.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/CangoAnimation-4v01.js"></script>

    <script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
    <script>
    window.onload=function(){
    brython(1);
    }
    </script>
</head>
<body>

<canvas id='gear1' width='800' height='750'></canvas>
 
<script type="text/python">
# 將 導入的 document 設為 doc 主要原因在於與舊程式碼相容
from browser import document as doc
# 由於 Python3 與 Javascript 程式碼已經不再混用, 因此來自 Javascript 的變數, 必須居中透過 window 物件轉換
from browser import window
# 針對 Javascript 既有的物件, 則必須透過 JSConstructor 轉換
from javascript import JSConstructor
import math
 
# 主要用來取得畫布大小
canvas = doc["gear1"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
# 針對類別的轉換, 將 Cango.js 中的 Cango 物件轉為 Python cango 物件
cango = JSConstructor(window.Cango)
# 針對變數的轉換, shapeDefs 在 Cango 中資料型別為變數, 可以透過 window 轉換
shapedefs = window.shapeDefs
# 目前 Cango 結合 Animation 在 Brython 尚無法運作, 此刻只能繪製靜態圖形
# in CangoAnimation.js
#interpolate1 = window.interpolate
# Cobi 與 createGearTooth 都是 Cango Javascript 程式庫中的物件
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="plotarea" 的 canvas 上
cgo = cango("gear1")
 
######################################
# 畫正齒輪輪廓
#####################################
def spur():
    # n 為齒數
    n = 17
    # pa 為壓力角
    pa = 25
    # m 為模數, 根據畫布的寬度, 計算適合的模數大小
    # Module = mm of pitch diameter per tooth
    m = 0.8*canvas.width/n
    # pr 為節圓半徑
    pr = n*m/2 # gear Pitch radius
    # generate gear
    data = creategeartooth(m, n, pa)
    # Brython 程式中的 print 會將資料印在 Browser 的 console 區
    #print(data)
    gearTooth = cobj(data, "SHAPE", {
            "fillColor":"#ddd0dd",
            "border": True,
            "strokeColor": "#606060" })
    gearTooth.rotate(180/n) # rotate gear 1/2 tooth to mesh
    # 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
    gear = gearTooth.dup()
    # gear 為單一齒的輪廓資料
    #cgo.render(gearTooth)
     
    # 利用單齒輪廓旋轉, 產生整個正齒輪外形
    for i in range(1, n):
        # 將 gearTooth 中的資料複製到 newTooth
        newTooth = gearTooth.dup()
        # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
        newTooth.rotate(360*i/n)
        # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
        gear.appendPath(newTooth, True) # trim move command = True
     
    # 建立軸孔
    # add axle hole, hr 為 hole radius
    hr = 0.6*pr # diameter of gear shaft
    shaft = cobj(shapedefs.circle(hr), "PATH")
    shaft.revWinding()
    gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
    cx = canvas.width/2
    cy = canvas.height/2
    gear.translate(cx, cy)
    # render 繪出靜態正齒輪輪廓
    cgo.render(gear)
    deg=math.pi/180
    Line=cobj(['M',cx,cy,'L',
        cx+pr*math.cos(180/n*deg),\
        cy+pr*math.sin(180/n*deg)],"PATH",{
         'strokeColor':'red','linewidth':2})
    cgo.render(Line)
spur()

</script>
</body>
</html>
'''
    return outstring
@ag1_40323107_cdw14.route('/spur2')
def spur2():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
 
<script>
window.onload=function(){
brython(1);
}
</script>
 
<canvas id='gear1' width='800' height='750'></canvas>
 
<script type="text/python">
# 將 導入的 document 設為 doc 主要原因在於與舊程式碼相容
from browser import document as doc
# 由於 Python3 與 Javascript 程式碼已經不再混用, 因此來自 Javascript 的變數, 必須居中透過 window 物件轉換
from browser import window
# 針對 Javascript 既有的物件, 則必須透過 JSConstructor 轉換
from javascript import JSConstructor
import math
 
# 主要用來取得畫布大小
canvas = doc["gear1"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
# 針對類別的轉換, 將 Cango.js 中的 Cango 物件轉為 Python cango 物件
cango = JSConstructor(window.Cango)
# 針對變數的轉換, shapeDefs 在 Cango 中資料型別為變數, 可以透過 window 轉換
shapedefs = window.shapeDefs
# 目前 Cango 結合 Animation 在 Brython 尚無法運作, 此刻只能繪製靜態圖形
# in CangoAnimation.js
#interpolate1 = window.interpolate
# Cobi 與 createGearTooth 都是 Cango Javascript 程式庫中的物件
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="plotarea" 的 canvas 上
cgo = cango("gear1")
 
######################################
# 畫正齒輪輪廓
#####################################
def spur(cx, cy, m, n, pa, theta):
    # n 為齒數
    #n = 17
    # pa 為壓力角
    #pa = 25
    # m 為模數, 根據畫布的寬度, 計算適合的模數大小
    # Module = mm of pitch diameter per tooth
    #m = 0.8*canvas.width/n
    # pr 為節圓半徑
    pr = n*m/2 # gear Pitch radius
    # generate gear
    data = creategeartooth(m, n, pa)
    # Brython 程式中的 print 會將資料印在 Browser 的 console 區
    #print(data)
 
    gearTooth = cobj(data, "SHAPE", {
            "fillColor":"#ddd0dd",
            "border": True,
            "strokeColor": "#606060" })
    #gearTooth.rotate(180/n) # rotate gear 1/2 tooth to mesh, 請注意 rotate 角度為 degree
    # theta 為角度
    gearTooth.rotate(theta) 
    # 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
    gear = gearTooth.dup()
    # gear 為單一齒的輪廓資料
    #cgo.render(gearTooth)
 
    # 利用單齒輪廓旋轉, 產生整個正齒輪外形
    for i in range(1, n):
        # 將 gearTooth 中的資料複製到 newTooth
        newTooth = gearTooth.dup()
        # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
        newTooth.rotate(360*i/n)
        # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
        gear.appendPath(newTooth, True) # trim move command = True
 
    # 建立軸孔
    # add axle hole, hr 為 hole radius
    hr = 0.6*pr # diameter of gear shaft
    shaft = cobj(shapedefs.circle(hr), "PATH")
    shaft.revWinding()
    gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
    gear.translate(cx, cy)
    # render 繪出靜態正齒輪輪廓
    cgo.render(gear)
    # 接著繪製齒輪的基準線
    deg = math.pi/180
    Line = cobj(['M', cx, cy, 'L', cx+pr*math.cos(theta*deg), cy+pr*math.sin(theta*deg)], "PATH", {
          'strokeColor':'blue', 'lineWidth': 1})
    cgo.render(Line)
 
# 3個齒輪的齒數
n1 = 15
n2 = 30
n3 = 15
n4 = 30
n5 = 15
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
# Module = mm of pitch diameter per tooth
# 利用 80% 的畫布寬度進行繪圖
# 計算模數的對應尺寸
m = canvas.width*0.8/(n1+n2+n3+n4+n5)
 
# 根據齒數與模組計算各齒輪的節圓半徑
pr1 = n1*m/2
pr2 = n2*m/2
pr3 = n3*m/2
pr4 = n4*m/2
pr5 = n5*m/2
# 畫布左右兩側都保留畫布寬度的 10%
# 依此計算對應的最左邊齒輪的軸心座標
cx = canvas.width*0.1+pr1
cy = canvas.height/2
 
# pa 為壓力角
pa = 25
 
# 畫最左邊齒輪, 定位線旋轉角為 0, 軸心座標 (cx, cy)
spur(cx, cy, m, n1, pa, 0)
# 第2個齒輪將原始的定位線逆時鐘轉 180 度後, 與第1個齒輪正好齒頂與齒頂對齊
# 只要第2個齒輪再逆時鐘或順時鐘轉動半齒的角度, 即可完成囓合
# 每一個齒分別包括從齒根到齒頂的範圍, 涵蓋角度為 360/n, 因此所謂的半齒角度為 180/n
spur(cx+pr1+pr2, cy, m, n2, pa, 180-180/n2)
# 第2齒與第3齒的囓合, 首先假定第2齒的定位線在 theta 角為 0 的原始位置
# 如此, 第3齒只要逆時鐘旋轉 180 度後, 再逆時鐘或順時鐘轉動半齒的角度, 即可與第2齒囓合
# 但是第2齒為了與第一齒囓合時, 已經從原始定位線轉了 180-180/n2 度
# 而當第2齒從與第3齒囓合的定位線, 逆時鐘旋轉 180-180/n2 角度後, 原先囓合的第3齒必須要再配合旋轉 (180-180/n2 )*n2/n3
spur(cx+pr1+pr2+pr2+pr3, cy, m, n3, pa, 180-180/n3+(180-180/n2)*n2/n3)
spur(cx+pr1+pr2+pr2+2*pr3+pr4, cy, m, n4, pa, 180-180/n3+(180-180/n3)*n3/n4)
spur(cx+pr1+pr2+pr2+2*pr3+2*pr4+pr5, cy, m, n5, pa, 180-180/n5+(180-180/n5)*n4/n5)

</script>
</body>
</html>
'''
    return outstring
