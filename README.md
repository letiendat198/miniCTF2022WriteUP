# MiniCTF 2022 Write-up

## Nội dung:

1. [Warm Up](https://github.com/letiendat198/miniCTFWriteUP/blob/master/README.md#1-warm-up)
- [1.1 Basic Forensics](https://github.com/letiendat198/miniCTFWriteUP/blob/master/README.md#11-basic-forensics) 
- [1.2 What is Netcat](https://github.com/letiendat198/miniCTFWriteUP/blob/master/README.md#12-what-is-netcat) 
- [1.3 Abcbof](https://github.com/letiendat198/miniCTFWriteUP/blob/master/README.md#13-abcbof) 
- [1.4 Rock, Paper, Scissors](https://github.com/letiendat198/miniCTFWriteUP#14-rock-paper-scissors)
2. [Web](https://github.com/letiendat198/miniCTFWriteUP#2-web)
- [2.1 PHP Moon Cake](https://github.com/letiendat198/miniCTFWriteUP#21-php-moon-cake)
- [2.2 Get out of here](https://github.com/letiendat198/miniCTFWriteUP#22-get-out-of-here)
- [2.3 Find Flag](https://github.com/letiendat198/miniCTFWriteUP#23-find-flag)
- [2.4 keiichi](https://github.com/letiendat198/miniCTFWriteUP#23-keiichi)
- [2.5 ISP Info]()
3. [Forensics](https://github.com/letiendat198/miniCTFWriteUP#3-forensics)
- [3.1 Correct File?]()
- [3.2 Japanese Food]()
- [3.3 Where is Nemo?]()
- [3.4 Are you Wibu??]()
- [3.5 OnlyFan]()
- [3.6 Love n Light]()
4. [Cryptography]()
- [4.1 Do you know what is basecrack]()
- [4.2 Love Song]()
- [4.3 Ceasar Knight]()
- [4.4 You are noob]()
- [4.5 ROTTOR]()
- [4.6 UwU]()
5. [Reverse Engineering]()
-  [5.1 Baby Kinzx]()
-  [5.2 EZ RE]()
-  [5.3 Loop Key]()
-  [5.4 XOR]()
-  [5.5 Lost Obfuscation]()
6. [Misc]()
-  [6.1 Best Avatar]()
-  [6.2 Base64]()
-  [6.3 New Misc]()
   
## 1. Warm Up
### 1.1 Basic Forensics

Đề bài cho chúng ta một file .svg. Đầu tiên hãy mở nó lên đã

![Circle](Warm_Up/Basic_Forensics/1.png)

Không có gì quá đặc biệt. Thử Inspect xem sao

![step2](Warm_Up/Basic_Forensics/2.png)

Ở trong block `\<text\>` ta có thể thấy được flag: `ISPCTF{7hAt_warm_up_gnys}`
	
### 1.2 What is Netcat

Netcat là một phần mềm có thể đọc và viết dữ liệu thông qua giao thức TCP hoặc UDP chủ yếu được điều khiển bởi các phần mềm và scripts khác (Để biết thêm, tham khảo `man nc`)
	
Đề bài cho chúng ta một câu lệnh của netcat. Hãy thử nhập vào terminal xem sao

```

$ nc 174.138.21.217 3136
	
                              NETCAT      
                            /\_____/\    
                           /  o   o  \   
                          ( ==  ^  == )   
                          ))         (    
                          (           )   
                         ( (  )   (  ) )  
                        (__(__)___(__)__) 
	

Here your flag: ISPCTF{Th1s_1s_n3t_c4t}

```

### 1.3 Abcbof
	
Vẫn là một câu lệnh netcat, nhập vào terminal thôi 

```
$ nc 174.138.21.217 3137
	
Hãy nhập tên người chơi: writeup
==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================
| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Tài Khoản | 5. Thoát Game |
======================================================================================

Hello writeup, chào mừng bạn đến với Game Bài Uy Tín Top 1 Việt Nam !!!
Nhập lựa chọn của bạn: 
2
==============Hướng Dẫn==============
  Chiến thắng để dành giải thưởng   
      1 triệu $ từ Halston <3       
                                    
 Mỗi lần nhập hãy nhập vào một lá   
  mà giống với lá bài của nhà cái   
  Bộ bài chỉ gồm 9 lá từ 2 đến 10    
 Do lợi nhuận cao nên mọi người đến 
 chơi bài rất nhiều dẫn đến khi đi  
 về họ cầm theo cả Át, J, Q, K để   
 đi về. Mỗi lần đoán đúng sẽ được   
             50 000$                
                                    
               Hint                 
  Hãy cố gắng nhập THẬT NHIỀU để    
      có thể chiến thắng nhé.       
                     Kevin Halston  
=====================================


```

Có vẻ như đây là một trò chơi, flag có trị giá 1 000 000 000$ mà mỗi lần thắng chỉ được có 50 000$. Nếu lần nào cũng thắng thì phải thắng 20000 lần. Oải ha. Thế chắc không chơi đúng luật được rồi. Đề bài còn cho kèm theo source code nữa kìa. Để xem có gì thú vị không.

Source rất dài nhưng chúng ta chỉ cần quan tâm phần đầu thôi. Cụ thể là đoạn này
```
long long money = 0;
puts("==========================Game Bai Doan So Uy Tin Doi Thuong ==========================");
puts("| 1. Choi Game   |  2. Huong Dan   |   3. Doi Flag   |  4. Thoat Game |  5. Tai Khoan |");
puts("======================================================================================");
puts("Hay nhap ten nguoi choi:");
char name[30];
gets(name);
system("clear");
```
Ta có thể thấy biến `name` là một char array có 30 phần tử. Vậy điều gì sẽ xảy ra nếu chúng ta nhập một chuỗi dài hơn 30 ký tự? Nó sẽ bị tràn, và tràn ra biến trước đó, là `long long money = 0`. Bằng cách này ta có thể hack tiền. Thử ha
				
```
Hãy nhập tên người chơi: 1111111111111111111111111111111111111111111111111111111111111
==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================
| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Tài Khoản | 5. Thoát Game |
======================================================================================

Hello 1111111111111111111111111111111111111111111111111111111111111, chào mừng bạn đến với Game Bài Uy Tín Top 1 Việt Nam !!!
Nhập lựa chọn của bạn:
3

Tài khoản của bạn có 3544668469065756977 $ 
=====================FLAG=======================
|Bạn có muốn mua FLAG với giá 1 000 000 000 $  |
|----------------------------------------------|
|         1. YES      |         2. NO          |
================================================
Lựa chọn của bạn : 
1


Chúc mừng bạn đã chiến thắng
Đây là Flag của bạn:
ISPCTF{B4s1c_Buff3r_0v3rFl0w}

```

### 1.4 Rock, Paper, Scissors
Lại là netcat. Nhập vào terminal nào

```
$ nc 174.138.21.217 3138
Welcome challenger to the game of Rock, Paper, Scissors
For anyone that beats me 5 times in a row, I will offer up a flag I found
Are you ready?
Type '1' to play a game
Type '2' to exit the program
```

Có vẻ ta phải thắng 5 lần thì mới lấy được flag. Khá khó ha. Nhưng không khó nữa nếu ta đoán được xem server sẽ ra gì. Xem source code nào

```
bool play () {
  char player_turn[100];
  srand(time(0));
  int r;

  printf("Please make your selection (rock/paper/scissors):\n");
  r = tgetinput(player_turn, 100);
  // Timeout on user input
  if(r == -3)
  {
    printf("Goodbye!\n");
    exit(0);
  }

  int computer_turn = rand() % 3;
  printf("You played: %s\n", player_turn);
  printf("The computer played: %s\n", hands[computer_turn]);

  if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
  } else {
    puts("Seems like you didn't win this time. Play again?");
    return false;
  }
}
```

Hàm `play()` ở trên được gọi ngay sau khi người chơi bấm 1. Nếu nhìn kỹ ta sẽ thấy hàm `srand()` được gọi trước lúc ta phải đưa ra lựa chọn

```
srand(time(0));
int r;

printf("Please make your selection (rock/paper/scissors):\n");
r = tgetinput(player_turn, 100);
```

Hàm `srand()` là hàm seed cho hàm `rand()`. Do đó nếu chúng ta biết được seed chúng ra sẽ biết được kết qua của hàm `rand()`. Và ở đây hàm `srand()` này được seed bằng hàm `time(0)` (Tức là số giây kể từ ngày 1/1/1970 cho tới nay) nói chung chỉ cần hiểu nó ám chỉ tới thời điểm hiện tại. Và may thay ta nằm cùng chỗ với server nên thời gian là như nhau. Tức là ta có thể tạo ra cùng một seed với server và đoán được server sẽ ra gì.
Vậy nên mình viết ra script sau

```
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char* hands[3] = {"rock", "paper", "scissors"};
    for(;;) {
        srand(time(0));
        int ran = rand() % 3;
        printf("Server will return: %s \n", hands[ran]);
        sleep(1);
    }
    return(0);
}
```

Script trên có tác dụng mỗi giây seed một lần và có thể đoán xem được trong giây này server sẽ ra gì. Ta chỉ cần chạy sccript này song song với netcat là có thể biết trước server sẽ ra gì và chúng ta có thể chiến thắng. 
(Lưu ý: Do timing mà script và server có thể lệch nhau từ 0-1s. Do đó cái mà server ra có thể là cái ở giây hiện tại cũng có thể là ở giây phía trước. Cần phải thử để biết được)

![Demo](Warm_Up/RPS/rps.gif)

Bây giờ chúng ta đã thắng được 5 lần rồi. Nhưng tại sao không thấy flag đâu nhỉ. Xem lại source code ha

```
if (wins >= 5) {
   puts("Congrats!!!");
   system("/bin/sh");
}
```

Sau khi thắng 5 lần thì server sẽ chạy command `/bin/sh` cho chúng ta access tới terminal chứ không đưa luôn flag cho chúng ta. Đầu tiên phải xem xung quanh có gì đã

```
ls
bin
chall
dev
flag.txt
ld.so
lib
lib32
lib64
libc.so.6
```

Chúng ta có thể thấy luôn có một file tên là `flag.txt`. Chắc đây là flag rồi.

```
cat flag.txt
ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}
```

<!-- (Đáng nhẽ em được first solve bài này nha nhưng mà lại bị báo sai. Đến tối thì lại được mà lúc đấy mất first solve rồi -.-) -->

## 2. Web
### 2.1 PHP Moon Cake

![First](Web/PHP_Moon_Cake/1.png)

Trang web này trông không có gì bất thường lắm nhỉ. Việc đầu tiên vẫn là Inspect thử xem sao nào

![First](Web/PHP_Moon_Cake/2.png)

Có thể thấy ở `<head>` có link tới một file css tên `/style_in.css`. Mở ra xem có manh mối gì không 

![First](Web/PHP_Moon_Cake/3.png)

Ở phần cuối có luôn flag kìa `ISPCTF{m00n_c4k3_15_t00_sw33t}`

### 2.2 Get out of here

![1](Web/GOOH/1.png)

Có vẻ như không có gì cả (Pun intended). Nhưng vẫn phải Inspect xem sao

![2](Web/GOOH/2.png)

Ồ flag ở kia luôn rồi: ` ISPCTF{jU5t_lnsp3ct_01012021dad}`

### 2.3 Find Flag

![1](Web/Find_Flag/1.png)

Một trong web không có gì bất thường và Inspect cũng không có manh mối gì cả. Sau khi mua hint thì ta biết được rằng flag được giấu ở `/flag.txt` 

![1](Web/Find_Flag/2.png)

Flag: `ISPCTF{HAv3_Fnu_Vvlt5_W3b}`

### 2.4 Keiichi

Trang web này Inspect giống như một mê cung vậy.

![1](Web/keiichi/1.png)

Vậy nên chúng ta hãy dùng search

![1](Web/keiichi/2.png)

Tìm thấy phần đầu của flag rồi. Sau khi nghịch bài Sqli blind thì mình mới để ý tới `robots.txt`. Thế nên quay lại thử xem sao

![1](Web/keiichi/3.png)

Và kia là phần 2 của flag. Sau một hồi ngắm nó thì có vẻ phần 2 của flag là một dạng url. Thử cho lên thanh url xem sao. 

![1](Web/keiichi/4.png)

Ồ có kết quả này. Nhìn dãy kia giống base64 ha. Sau khi giải ra sẽ được phần cuối của flag 

 ![1](Web/keiichi/5.png)
 
 Vậy cuối cùng flag là: `ISPCTF{H3_1S_C0m3B4ck_Y0u_Can_find_him}`
 
 ### 2.5 ISP Info
 
 Đề bài cho chúng ta một trang web mà chỉ ISPER mới có thể truy cập
 
 ![1](Web/ISP_Info/1.png)
 
 Hmmm, muốn giả làm ISPER thì chắc phải thay đổi Request đến server thôi. Cụ thể là `User-Agent`. Dùng Burp Suite để làm việc này he.
 
  ![1](Web/ISP_Info/2.png)
 
 Có thể thấy dòng `User-Agent` đang là Mozilla Firefox. Phải sửa lại thôi
 
  ![1](Web/ISP_Info/3.png)
  Như này chắc là được rồi nhỉ. Forward tới Server xem phản ứng như thế nào thôi.
  
   ![1](Web/ISP_Info/4.png)
   
   Có thay đổi rồi kìa. Lần này trang web lại hỏi chúng ta xem có biết Facebook của CLB ISP không kìa. Để thể hiện là mình biết thì chắc chắn là phải được đích thân trang Facebook của ISP giới thiệu rồi. Cái này cũng fake được nữa nè. Dùng Header `Referer`. Quay trở lại với Burp Suite nào
   
   ![1](Web/ISP_Info/5.png)
   Như vậy là được rồi. Chắc không bị lộ đâu. Để xem Server thấy sao nhỉ.
   
   ![1](Web/ISP_Info/6.png)
   
   Hmmm, địa chỉ localhost của mình à. Chắc hẳn là `127.0.0.1` rồi. Vậy làm sao để trả lời Server bây giờ? Dùng Header `X-Forwarded-For` chứ còn gì nữa.
   
   ![7](Web/ISP_Info/7.png)
   Được rồi để xem có flag chưa.
   
   ![8](Web/ISP_Info/8.png)
   
   Lại là câu hỏi nữa. Để xem nào, Khoa ATTT PTIT thành lập vào Thứ 3, 05/04/2022 (Dạ làm riết cái bài này rồi em thuộc luôn đó). Để trả lời thì dùng Header `Date` là được rồi.
   
   ![9](Web/ISP_Info/9.png)
   Để xem câu đố tiếp theo là gì nào. 
   ![10](Web/ISP_Info/10.png)
   
   Để thể hiện trình độ Tiếng Việt của bản thân thì phải dùng header `Accept-Language` rồi. Nhưng mà không phải `vi-VN,vi` mà là `vi-vi,vi`
   
   ![11](Web/ISP_Info/11.png)
   Cuối cùng thì cũng xong rồi
   ![12](Web/ISP_Info/12.png)
   
   Flag: `ISPCTF{N0w_Y0u_Kn3w_4b0ut_ISP_Y0ur_W3lC0m3}`
  
 
## 3. Forensics

### 3.1 Correct File?

Đề bài cho chúng ta một file có tên `file.zip`. Hãy thử giải nén nó ra đã. 
Chúng ta sẽ có một file `file.mp3`. Nếu Media Player của bạn thông minh (Như VLC và vài cái nữa chẳng hạn) thì có lẽ đã thấy video chứa flag rồi. Nhưng nếu không thì hãy thử check xem file này có đúng là file `mp3` không nhé. Trong đa số các trường hợp thì dùng câu lệnh `file` là đủ rồi.

```
$ file file.mp3                                       
file.mp3: ISO Media, MP4 v2 [ISO 14496-14]
```

Vậy là lộ rồi. Đây rõ ràng là một file `mp4`. Đổi lại đuôi file thành `.mp4` để thấy flag thôi.

Flag: `ISPCTF{i_am_following_you}`

### 3.2 Japanese Food

Đề bài đưa ta đến một MV của Chipu. Và đừng như mình `xem đi xem lại 5-6 lần` để ghép flag mà hãy xem đến cuối video, nơi mà một mã QR chứa flag đang đợi bạn. Bài học rút ra là hãy luôn xem đến hết video.

![1](Forensics/Japanese_Food/1.png)

Flag: `ISPCTF{Pe0ple_mAke_1t_complicat3d}`

### 3.3 Where is Nemo

Đề bài cho chúng ta một file `jpg` (Ủa mình nhớ lúc mình làm là file `webp` mà nhỉ). Nhưng mà thôi không sao, cái mấu chốt là file `jpg` này mở không được (Hoặc ít nhất là phần mềm xem ảnh của mình không mở được). Khả nghi nhỉ. Hãy dùng `file` thử xem 
```
$ file Where_is_Nemo.jpg
Where_is_Nemo.jpg: RIFF (little-endian) data, Web/P image, VP8 encoding, 1600x1200, Scaling: [none]x[none], YUV color, decoders should clamp
```

Thì ra đây là file `webp` thảo nào không mở được nhỉ. Nhưng vẫn thấy khả nghi, thôi dùng `binwalk` cho chắc

```
$ binwalk Where_is_Nemo.jpg                               

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
140384        0x22460         RAR archive data, version 5.x
274255        0x42F4F         TIFF image data, big-endian, offset of first image directory: 8
274281        0x42F69         RAR archive data, version 5.x
363715        0x58CC3         RAR archive data, version 5.x
400673        0x61D21         RAR archive data, version 5.x
```

Vậy là lộ hết luôn rồi. Hóa ra đây thực chất là file `rar`, bên trong chưa 3 file `rar` nữa. Giải nén thôi

```
$ unrar x Where_is_Nemo.jpg

UNRAR 6.12 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from Where_is_Nemo.jpg

Extracting  crush.jpg                                                 OK 
All OK
```

Giải nén xong lại có một file `crush.jpg` kìa. Theo như `binwalk` thì đây thực chất vẫn là file `rar` thôi. Lại giải nén tiếp

```
$ unrar x crush.jpg        

UNRAR 6.12 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from crush.jpg

Extracting  marlin.jpg                                                OK 
All OK
```

Lại ra một file nữa tên `marlin.jpg`. Nhưng mà vẫn vậy, giải nén tiếp

```
$ unrar x marlin.jpg     

UNRAR 6.12 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from marlin.jpg

Extracting  dory.jpg                                                  OK 
All OK
```

Ra một file tên `dory.jpg`. File này có lẽ là file `rar` giả mạo thứ 3 mà `binwalk` nhắc đến rồi. Giải nén nốt thôi

```
$ unrar x dory.jpg  

UNRAR 6.12 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from dory.jpg

Extracting  nemo.txt                                                  OK 
All OK
```

File `txt` gì mà mở lên lại toàn kí tự lạ không đọc được. Chắc lại là hàng fake rồi. Thử dùng `file` xem. 

```
$ file nemo.txt             
nemo.txt: JPEG image data, JFIF standard 1.01, resolution (DPI), density 120x120, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=1, orientation=upper-left], baseline, precision 8, 2000x3000, components 3
```

Thì ra đây là một file `.jpeg`. Đổi lại đuôi file và mở lên thôi

![1](Forensics/Where_is_Nemo/nemo.jpeg)
Flag: `ISPCTF{y0u_5ave_Nem0_f15h}`

### 3.4 Are you Wibu

Đề bài cho chúng ta một file ảnh `Are_u_wibu.jpeg`. Mở lên bình thường, `file` và `binwalk` cũng thấy không có gì bất thường. Vậy nhìn nội dung đã

![1](Forensics/AYWB/Are_u_wibu.jpeg)


Có chữ gì đó nhưng bị xáo trộn lên hết rồi. Nếu để ý kỹ ta có thể thấy được sự liên quan giữa các dòng

![2](Forensics/AYWB/1.jpeg)

Cứ cách 2 dòng lại có một dòng liên quan đến nhau (Phần màu đỏ). Thử ghép chúng lại với nhau xem có đọc được chữ không nhé

![2](Forensics/AYWB/2.jpeg)

Có chữ đọc được rồi này `ISPCTF{w1bu_n3`. Có vẻ mới chỉ có phần đầu của flag thôi. Phần sau chắc chắn vẫn còn ở trong bức ảnh này. Vẫn còn các dòng mà mình chưa dùng mà. Vẫn vậy, cứ cách 2  dòng lại có một dòng liên quan đến nhau, lần này là các dòng ở phía trên các dòng trước (Phần màu xanh)

![2](Forensics/AYWB/3.jpeg)

Hãy thử ghép chúng lại với nhau xem 

![2](Forensics/AYWB/4.jpeg)
Ra vế sau của flag rồi `v3r_d13_1337}`. Vậy cuối cùng flag là `ISPCTF{w1bu_n3v3r_d13_1337}`

### 3.5 OnlyFan

Đề bài cho chúng ta một dòng chữ bị swirl khá là nặng

![1](Forensics/OF/Round.png)
Nhưng rất may là swirl có thể đảo ngược được. Trong lúc tìm cách thì mình thấy có cái tool online này làm rất tốt luôn này `https://www.photo-kako.com/en/swirl/`

![2](Forensics/OF/1.png)

Muốn unswirl thì phải chỉnh `Angle` về giá trị âm chứ nhỉ 

![2](Forensics/OF/2.png)

Bắt đầu đọc được chữ rồi. Lưu về máy và làm lại thêm một lần nữa là ra kết quả rồi.

![2](Forensics/OF/3.png)

Flag: `ISPCTF{r0und_n_r0und_1908absc}`

### 3.6 Love n Light

Đề bài cho chúng ta một file ảnh nhìn khá bình thường cũng không có manh mối gì cả, `file` và `binwalk` kể cả `xxd` (hex dump) cũng không có gì bất thường. Vậy chắc vấn đề phải ở trong chính bức ảnh rồi. Mình tìm thấy một tool Forensics online khá hay ho `https://29a.ch/photo-forensics/`

![1](Forensics/LnL/1.png)

Mở vào phần Error Level Detection (Theo như khả năng đọc hiểu của mình thì là để xem xem ảnh có bị chỉnh sửa chỗ nào không vì nếu bị chỉnh sửa thì Error Level sẽ khác các phần còn lại của ảnh)

![1](Forensics/LnL/2.png)

Flag kia rồi: `ISPCTF{Fr0m_kA1z_w1tH_L0v3}`


## 4 Cryptography


