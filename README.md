# titanic 

variaty dosyası ile her sütunda kaç farklı değer olduğu incelendi. En fazla çeşit 891 adet ile PasengerId sütununda olduğu gözüküyordu ki her yolcunun farklı bir passenger id ye sabit olması beklenen bir şeydir. Bu sebeple PasengerId göz ardı edilecektir. Benzer sebelerle Name ve Ticket sütunu da analize dahil edilmeyecektir. 

Cabin sütunundaki 148 ifadenin baş harfleri yolcuların geminin hangi seviyesinde bulunduğunu belirtmektedir. Öncelikle bu kodlar sayılardan arındırıldı. Ardından hayatta kalmaya bir etkisinin olup olmadığı incelendi. Benzer şekilde Embarked Pcalass ve Sex sütunlarının hayatta kalmaya etkisi olup olmadığı incelendi.

Cabin

unk number: 687 survive_rate: 0.29985443959243085

C number: 59 survive_rate: 0.5932203389830508

E number: 32 survive_rate: 0.75

G number: 4 survive_rate: 0.5

D number: 33 survive_rate: 0.7575757575757576

A number: 15 survive_rate: 0.4666666666666667

B number: 47 survive_rate: 0.7446808510638298

F number: 13 survive_rate: 0.6153846153846154

T number: 1 survive_rate: 0.0

cabin kodu bilinmeyen yolcu sayısı oldukça yüksek olmakla beraber hayatta kalma oranları kabin kodu bilinen yolculara kıyasla oldukça

Embarked

S number: 644 survive_rate: 0.33695652173913043

C number: 168 survive_rate: 0.5535714285714286

Q number: 77 survive_rate: 0.38961038961038963

unk number: 2 survive_rate: 1.0

Pclass

3 number: 491 survive_rate: 0.24236252545824846

1 number: 216 survive_rate: 0.6296296296296297

2 number: 184 survive_rate: 0.47282608695652173

Sex

male number: 577 survive_rate: 0.18890814558058924

female number: 314 survive_rate: 0.7420382165605095


