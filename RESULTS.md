# Results

In this document, we will technically explain how the greedy K-Center algorithm works and the results obtained.

## Algorithm Description

The K-Center Problem involves placing a specified number of facilities and assigning each customer to their nearest facility. The objective is to minimize the maximum distance between any customer and their assigned facility. This problem is commonly encountered in energy distribution, logistics, and service network optimization.

### Step-by-Step Greedy K-Center Algorithm

1. **Initialization**: Determine all potential facility locations and their associated costs. Potential locations are selected based on customer demands and logistical advantages.

2. **Initial Center Selection**: In the first step, select the initial facility location that minimizes the maximum distance to the farthest customer. This step ensures starting with the facility closest to most customers.

3. **Iterative Selection of K Centers**: Repeat the following steps until K facilities are selected:
    - **Selecting a New Center**: Keeping the current facility locations fixed, select a new facility location from the remaining potential locations. The selection aims to minimize the maximum distance to the farthest customer.
    - **Customer Assignments**: In each iteration, reassign all customers to the existing open facilities. Each customer is assigned to the nearest facility, minimizing the total distance.
    - **Performance Evaluation**: Evaluate the performance of the newly selected facility and determine if it provides the optimal location. Make necessary improvements if required.

## Example Application and Results

Let's examine how the algorithm works through an example:

### Data Preparation

Potential charging station locations in various neighborhoods of Istanbul are identified. The locations of electric vehicle owners and distances from these locations to potential station sites are analyzed.

- **Black Triangles**: Represent possible charging station locations.
- **Colored Triangles**: Represent open stations and the color indicates which area they serve.
- **Colored Points**: Represent customers connected to each colored station.
- **Gray Points**: Represent customers who do not receive service.

### Initial Center Selection

The first facility is selected to minimize the maximum distance to the farthest customer. For example, a customer in Kadıköy may have the nearest facility in Üsküdar.

![Data Preparation](./images/first-station.png)

### Selection of New Centers and Customer Assignments

The second facility is selected, keeping the current facility (Üsküdar) fixed. For example, a new facility may be located in Beşiktaş. All customers are then reassigned to the nearest facilities, such as Üsküdar and Beşiktaş.

![Initial Center Selection](./images/graph.png)

### Performance Evaluation and Final Improvements

Similar steps are followed to select the third and fourth facilities, ensuring all customers are assigned to the nearest facilities to minimize total distance. Ultimately, K facilities are selected across various neighborhoods of Istanbul to minimize the maximum distance between customers and facilities.

## Evaluation of Results

This greedy algorithm provides a fast and effective solution to the K-Center Problem. By optimally placing a specified number of facilities, it enhances customer satisfaction and reduces logistical costs. EnerjiCo successfully used this algorithm to identify and establish the most efficient charging station locations in Istanbul, improving service delivery to electric vehicle owners.

---

This technical explanation covers the operation of the greedy K-Center algorithm used by EnerjiCo to establish new charging stations in Istanbul and evaluates the outcomes achieved.

---
---

# Sonuçlar

Bu dosyada, K-Merkez Problemi için kullanılan açgözlü algoritmanın nasıl çalıştığını ve elde edilen sonuçları teknik olarak açıklayacağız.

## Algoritma Açıklaması

K-Merkez Problemi, belirli sayıda tesisin konumlandırılması ve her müşterinin en yakın tesise atanması ile ilgilidir. Amaç, en uzak müşteri-tesis mesafesini minimize etmektir. Bu problem, özellikle enerji dağıtım, lojistik ve servis ağları gibi alanlarda yaygın olarak karşılaşılan bir sorundur.

### Adım Adım Açgözlü K-Merkez Algoritması

1. **Başlangıç Adımı**: Tüm potansiyel tesis konumları ve bu konumların maliyetleri belirlenir. Potansiyel konumlar, müşteri talepleri ve lojistik avantajlar göz önünde bulundurularak seçilir.

2. **İlk Merkez Seçimi**: İlk adımda, en uzak müşteriye olan mesafeyi minimize eden ilk tesis konumu seçilir. Bu adım, müşterilere en yakın merkezi seçerek başlamayı sağlar.

3. **K Merkez Seçilene Kadar Tekrarlama**: Seçilen ilk merkezden sonra, aşağıdaki adımlar K tesis seçilene kadar tekrarlanır:
    - **Yeni Merkez Seçimi**: Mevcut tesislerin konumları sabit tutularak, kalan potansiyel tesisler arasından yeni bir merkez seçilir. Yeni merkezin seçimi, en uzak müşteriye olan mesafeyi minimize edecek şekilde yapılır.
    - **Müşteri Atamaları**: Her iterasyonda, tüm müşteriler mevcut açık tesisler arasında yeniden atanır. Her müşteri, en yakın tesise atanarak toplam mesafe minimize edilir.
    - **Performans Değerlendirmesi**: Yeni seçilen tesisin performansı değerlendirilir ve en uygun konum olup olmadığı kontrol edilir. Gerekiyorsa iyileştirmeler yapılır.

### Örnek Uygulama ve Sonuçlar

Bir örnek üzerinden algoritmanın nasıl çalıştığını inceleyelim:

#### Veri Hazırlığı

İstanbul'daki çeşitli semtlerde potansiyel şarj istasyonu yerleri belirlenmiştir. Elektrikli araç sahiplerinin konumları ve bu konumlardan potansiyel istasyon yerlerine olan mesafeler analiz edilmiştir.

- **Siyah Üçgenler:** Açılabilecek olan şarj istasyonu yerlerini temsil eder.
- **Renkli Üçgenler:** Açılmış olan istasyonları ve hangi renge hizmet verdiklerini gösterir.
- **Renkli Noktalar:** Her bir renkli istasyona bağlı müşterileri gösterir.
- **Gri Noktalar:** Hizmet alamayan müşterileri temsil eder.

#### İlk Merkez Seçimi

İlk tesis, en uzak müşteriye olan mesafeyi minimize edecek şekilde seçilir. Örneğin, Kadıköy'de bulunan bir müşteriye en yakın tesis Üsküdar'da olabilir.

![Veri Hazırlığı](./images/first-station.png)

#### Yeni Merkez Seçimi ve Müşteri Atamaları

İkinci tesis, mevcut tesis (Üsküdar) sabit tutularak seçilir. Yeni tesis, örneğin Beşiktaş'ta olabilir. Tüm müşteriler, Üsküdar ve Beşiktaş tesisleri arasında en yakın olanına atanır.

![İlk Merkez Seçimi](./images/graph.png)

#### Performans Değerlendirmesi ve Son İyileştirmeler

Üçüncü ve dördüncü tesisler de benzer şekilde seçilir ve tüm müşteriler en yakın tesise atanarak toplam mesafe minimize edilir. Sonuçta, İstanbul'un çeşitli semtlerinde seçilen K tesis, en uzak müşteri-tesis mesafesini minimize edecek şekilde konumlandırılmış olur.

### Sonuçların Değerlendirilmesi

Bu açgözlü algoritma, K-Merkez Problemi için hızlı ve etkili bir çözüm sunar. Algoritmanın performansı, belirli sayıda tesisin optimal konumlandırılmasını sağlayarak müşteri memnuniyetini artırır ve lojistik maliyetleri düşürür. EnerjiCo, bu algoritmayı kullanarak İstanbul'da en verimli şarj istasyonu yerlerini belirleyip kurmuş ve elektrikli araç sahiplerine daha iyi hizmet sunmuştur.

---

Bu teknik açıklama, EnerjiCo'nun İstanbul'da yeni şarj istasyonları kurma sürecinde kullandığı açgözlü K-Merkez algoritmasının nasıl çalıştığını ve elde edilen sonuçların değerlendirilmesini kapsamaktadır.
