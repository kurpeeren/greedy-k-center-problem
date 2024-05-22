# Tesis Yerleşimi Problemi - SimitCo

## Problem Tanımı

SimitCo, İstanbul çevresinde belirli sayıda fırın tesisi açmayı hedefleyen bir pastacılık şirketidir. Şirket mühendisleri, tesisler için çeşitli aday lokasyonları ve müşteri konumlarını belirlemiş, ancak uzun vadeli kararlarını tek başlarına vermekten çekinmişlerdir. Bu noktada, iyi performans gösteren bir buluşsal yöntem oluşturmak amacıyla aşağıdaki adımları izlemeye karar verdiniz.

## Algoritma: K-Merkez Problemi için Açgözlü Bir Algoritma

1. **Konumlandırma:** Toplam sayım kullanılarak en uygun 1 merkezli konumdaki ilk tesis belirlenir.
2. **K merkez tespit ettik (açtık) mı?** Hayır ise:
   - Açık merkezlerin konumlarını sabit tutarak bir sonraki merkezi en uygun konuma (toplam numaralandırmayı kullanarak) yerleştirin.
   - Müşteriler açık tesisler arasında yeniden atanır.
3. Bu adımlar, tüm K merkez açılana kadar devam eder.

## Sorular ve Cevaplar

### 1. Bu ne tür bir Tesis Yerleşimi sorunudur? Neden?

Bu, **K-Merkez Problemi (K-Center Problem)** olarak adlandırılan bir Tesis Yerleşimi problemidir.

**Neden?**

- **Müşterilerin Uzaklığı:** SimitCo'nun her müşterisiyle uzun vadeli sözleşmeleri olduğundan, müşteri verileri belirleyicidir ve her müşterinin en yakın tesise olan uzaklığının minimum olması hedeflenmektedir.
- **Belirli Sayıda Tesis:** Şirket, İstanbul çevresinde belirli sayıda fırın tesisi açmayı planlıyor. Bu da belirli (K) sayıda tesisin yerleştirileceğini gösterir.
- **Performans:** Açgözlü (greedy) bir algoritma kullanarak merkezlerin konumlarını belirlemek, K-Merkez Problemi için yaygın bir yaklaşımdır. Bu algoritma, mevcut en uygun konumu seçerek ve her adımda toplam numaralandırmayı kullanarak müşteri atamalarını günceller.

Bu nedenle, bu problem K-Merkez Problemi'nin tipik özelliklerini taşıdığı için bu tür bir Tesis Yerleşimi sorunu olarak tanımlanabilir.
