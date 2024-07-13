# Facility Location Problem - EnerjiCo

## Problem Statement

EnerjiCo is an energy company aiming to open a specified number of electric vehicle charging stations around Istanbul. The company engineers have identified various candidate locations for stations and customer locations, but they are hesitant to make long-term decisions on their own. At this point, you have decided to follow the steps below to develop a well-performing heuristic method.

## Algorithm: Greedy Algorithm for K-Center Problem

1. **Initialization:** Determine the optimal initial location for the first station using the total count.
2. **Have we identified (opened) K centers yet?** If not:
   - Keep the locations of open centers fixed and place the next center in the optimal position (using the total numbering).
   - Customers are reassigned among open facilities.
3. These steps continue until all K centers are opened.

## Questions and Answers

### 1. What type of Facility Location problem is this? Why?

This is a **K-Center Problem**, a type of Facility Location problem.

**Why?**

- **Customer Distances:** EnerjiCo has long-term contracts with each customer, making customer data decisive, and aiming to minimize the distance to the nearest station for each customer.
- **Specified Number of Facilities:** The company plans to open a specified number of charging stations around Istanbul, indicating a specific (K) number of facilities to be placed.
- **Performance:** Using a greedy algorithm to determine the locations of centers by selecting the current optimal location and updating customer assignments using total numbering at each step.

Therefore, this problem can be classified as a Facility Location problem typical of the K-Center Problem due to these characteristics.

## Files

- `Setup.py`: Includes project configuration and manages dependencies.
- `Point.py`: Contains classes for defining and processing point (customer) data.
- `Operators.py`: Includes various operations and operators for the K-center algorithm.
- `Facility.py`: Contains classes for defining and processing facility (center) data.
- `LICENSE`: Contains licensing information for the project.
- `README.md`: Includes project description and usage instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact me at kurpeeren@gmail.com.


---

# Tesis Yerleşimi Problemi - EnerjiCo

## Problem Tanımı

EnerjiCo, İstanbul çevresinde belirli sayıda elektrikli araç şarj istasyonu açmayı hedefleyen bir enerji şirketidir. Şirket mühendisleri, istasyonlar için çeşitli aday lokasyonları ve müşteri konumlarını belirlemiş, ancak uzun vadeli kararlarını tek başlarına vermekten çekinmişlerdir. Bu noktada, iyi performans gösteren bir buluşsal yöntem oluşturmak amacıyla aşağıdaki adımları izlemeye karar verdiniz.

## Algoritma: K-Merkez Problemi için Açgözlü Bir Algoritma

1. **Konumlandırma:** Toplam sayım kullanılarak en uygun 1 merkezli konumdaki ilk istasyon belirlenir.
2. **K merkez tespit ettik (açtık) mı?** Hayır ise:
   - Açık merkezlerin konumlarını sabit tutarak bir sonraki merkezi en uygun konuma (toplam numaralandırmayı kullanarak) yerleştirin.
   - Müşteriler açık tesisler arasında yeniden atanır.
3. Bu adımlar, tüm K merkez açılana kadar devam eder.

## Sorular ve Cevaplar

### 1. Bu ne tür bir Tesis Yerleşimi sorunudur? Neden?

Bu, **K-Merkez Problemi (K-Center Problem)** olarak adlandırılan bir Tesis Yerleşimi problemidir.

**Neden?**

- **Müşterilerin Uzaklığı:** EnerjiCo'nun her müşterisiyle uzun vadeli sözleşmeleri olduğundan, müşteri verileri belirleyicidir ve her müşterinin en yakın istasyona olan uzaklığının minimum olması hedeflenmektedir.
- **Belirli Sayıda Tesis:** Şirket, İstanbul çevresinde belirli sayıda şarj istasyonu açmayı planlıyor. Bu da belirli (K) sayıda tesisin yerleştirileceğini gösterir.
- **Performans:** Açgözlü (greedy) bir algoritma kullanarak merkezlerin konumlarını belirlemek, K-Merkez Problemi için yaygın bir yaklaşımdır. Bu algoritma, mevcut en uygun konumu seçerek ve her adımda toplam numaralandırmayı kullanarak müşteri atamalarını günceller.

Bu nedenle, bu problem K-Merkez Problemi'nin tipik özelliklerini taşıdığı için bu tür bir Tesis Yerleşimi sorunu olarak tanımlanabilir.


## Dosyalar

- `Setup.py`: Proje yapılandırması ve bağımlılıkların yönetimini içerir.
- `Point.py`: Nokta (müşteri) verilerinin tanımlandığı ve işlendiği sınıfları içerir.
- `Operators.py`: K-merkez algoritmasının çeşitli işlemlerini ve operatörlerini içerir.
- `Facility.py`: Tesis (merkez) verilerinin tanımlandığı ve işlendiği sınıfları içerir.
- `LICENSE`: Projenin lisans bilgilerini içerir.
- `README.md`: Proje açıklaması ve kullanım talimatlarını içerir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen Pull Request gönderin.

## İletişim

Herhangi bir soru veya öneriniz için lütfen bir sorun açın veya bana kurpeeren@gmail.com adresinden ulaşın.
