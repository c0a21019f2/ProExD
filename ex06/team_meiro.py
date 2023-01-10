### インポート
import sys
import random
import pygame as pg
#from pygame.locals import *
 
### 定数
B_SIZE = 40     # ブロック辺長
C_SIZE = 40     # キャラクターサイズ
M_DOT  = 40     # 移動ドット
W_TIME = 20     # 待ち時間
WIDTH_brock = 16 #横のブロックの数
HEIGHT_brock = 16 #縦のブロックの数
WIDTH  = WIDTH_brock * B_SIZE  # 画面横サイズ
HEIGHT = HEIGHT_brock * B_SIZE   # 画面縦サイズ

F_SIZE = 60     # フォントサイズ
 
### 迷路マップの生成
def make_maze(yoko, tate):
    global maze_lst

    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]


    maze_lst = [[1 for i in range(tate)] for j in range(yoko)]  #大きさがtate*yokoの「1」の2次元リスト
    for maze_yoko in range(1, len(maze_lst)-1): #壁ではない部分を0にする
        for cell in range(1, len(maze_lst[0])-1):
            maze_lst[maze_yoko][cell] = 0
    for y in range(2, tate-2, 2): #迷路を作る
        for x in range(2, yoko-2, 2):
            maze_lst[x][y] = 1
            if x > 2:
                rnd = random.randint(0, 2)
            else:
                rnd = random.randint(0, 3)
            maze_lst[x+YP[rnd]][y+XP[rnd]] = 1
    maze_lst[x+2][y+2] = 2  #一番右下にゴールの生成

    return maze_lst


### 迷路生成のクラス
class Maze(pg.sprite.Sprite):#引数にSpriteを取る
 
    ### 初期化メソッド
    def __init__(self, name, x, y):
        pg.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pg.image.load(name).convert()
 
        ### 画像サイズ変更
        self.image = pg.transform.scale(self.image, (B_SIZE, B_SIZE))
 
        ### キャラクターオブジェクト生成
        self.rect = self.image.get_rect()
 
        ### ブロック位置設定
        self.rect.left = x * (self.rect.width)
        self.rect.top  = y * (self.rect.height)
 
    ### 迷路描画
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
### こうかこんを作るCharacterクラス
class Character(pg.sprite.Sprite):#引数にsprite
 
    ### 初期化メソッド
    def __init__(self, name):
        pg.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pg.image.load(name).convert_alpha()
 
        ### 画像サイズ変更
        self.image = pg.transform.scale(self.image, (C_SIZE, C_SIZE))
 
        ### キャラクターオブジェクト生成
        self.rect = self.image.get_rect()
 
    
    ### こうかこんの場所の更新
    def update(self, char_x, char_y):
 
        ### こうかこんの位置
        self.rect.centerx = char_x
        self.rect.centery = char_y
 
    ### こうかこんの描画
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
### main関数
def main():
    global maze_lst
 
    ### マップ座標
    row = col = 0
 
    ### 座標初期化
    x = y = 0
 
    ### 画面初期化
    pg.init()
    surface = pg.display.set_mode((WIDTH,HEIGHT))
    rect = surface.get_rect()
    
 
    ### 迷路グループ作成
    make_maze(WIDTH_brock,HEIGHT_brock)

    blocks = pg.sprite.Group()
    for b1 in maze_lst:      # 1次元リスト
        for b2 in b1:       # 2次元リスト
            if   b2 == 0:
                blocks.add(Maze("fig/pg_bg.jpg", x, y))#床背景の追加
            elif b2 == 1:
                blocks.add(Maze("fig/shot.gif", x, y))#壁背景の追加
            elif b2 == 2:
                blocks.add(Maze("fig/2.png", x, y))#ゴール背景の追加
            x += 1
 
        ### 座標更新
        else:
            x  = 0
            y += 1
 
    blocks.draw(surface)
 
    ### Characterクラスのこうかこんの作成
    character = Character("fig/3.png")
 
    ### キャラクター初期位置
    char_x, char_y = int(C_SIZE+(C_SIZE / 2)), int(C_SIZE+(C_SIZE / 2))
 
    ### 無限ループ
    while True:
 
        ### 未ゴール時の処理
        if maze_lst[row+1][col+1] != 2:
 
            ### 迷路描画
            blocks.draw(surface)
 
            ### こうかこんの更新
            character.update(char_x, char_y)
            character.draw(surface)
 
        ### ゴール時の処理
        else:
            ### テキスト設定
            font = pg.font.Font(None, F_SIZE)
            text = font.render("GOAL!", True, (224,224,255))
 
            ### ゴール描画
            surface.fill((0,0,0))
            surface.blit(text, [HEIGHT/2,WIDTH/2])
 
        ### 画面更新
        pg.display.update()
 
        ### 待ち時間
        pg.time.wait(W_TIME)
 
        ### イベント取得
        for event in pg.event.get():
            if event.type==pg.QUIT:#辞める時の処理
                exit()
            if event.type==pg.KEYDOWN:#何かキーを触ったら
                pressed = pg.key.get_pressed() # 辞書型
                if pressed[pg.K_ESCAPE]:#エスケープキーでゲーム終了
                    exit()
                if pressed[pg.K_LEFT]:#こうかこんの場所とマップの更新
                    if (char_x > 0      + (C_SIZE*2)) and (maze_lst[row+1][col] != 1):
                        col -= 1
                        char_x -= M_DOT
                if pressed[pg.K_RIGHT]:#こうかこんの場所とマップの更新
                    if (char_x < WIDTH  - (C_SIZE*2)) and (maze_lst[row+1][col+2] != 1):
                        col += 1
                        char_x += M_DOT
                if pressed[pg.K_UP]:#こうかこんの場所とマップの更新
                    if (char_y > 0      + (C_SIZE*2)) and (maze_lst[row][col+1] != 1):
                        row -= 1
                        char_y -= M_DOT
                if pressed[pg.K_DOWN]:#こうかこんの場所とマップの更新
                    print("in")
                    if (char_y < HEIGHT - (C_SIZE*2)) and (maze_lst[row+2][col+1] != 1):
                        row += 1
                        char_y += M_DOT
                print(char_y, char_x)
 
### 終了関数
def exit():
    pg.quit()
    sys.exit()
 
### メイン関数呼び出し
if __name__ == "__main__":  
    ### 処理開始
    main()