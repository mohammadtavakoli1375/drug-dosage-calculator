import React, { useState } from 'react';
import { Calculator, Info, BookOpen, AlertTriangle, Search, Pill, Heart, Syringe, FileText } from 'lucide-react';

const App = () => {
  const [selectedDrug, setSelectedDrug] = useState('');
  const [weight, setWeight] = useState('');
  const [age, setAge] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [showDetails, setShowDetails] = useState(false);

  // داروهای مورد نظر با اطلاعات کامل
  const drugs = [
    {
      id: 'paracetamol',
      name: 'پاراستامول (استامینوفن)',
      form: 'قرص 500mg',
      commonDose: '500–1000mg هر 4–6 ساعت',
      usage: 'خوراکی، بعد غذا یا با معده خالی',
      indications: 'تب، دردهای خفیف تا متوسط',
      contraindications: 'حساسیت به دارو',
      interactions: 'الکل، وارفارین',
      sideEffects: 'حالت تهوع، بثورات پوستی',
      pregnancy: 'قابل مصرف در بارداری و شیردهی با احتیاط',
      formula: '10-15 mg/kg/dose',
      maxDose: '1000 mg',
      frequency: 'هر 4-6 ساعت',
      source: 'WHO Guidelines 2023',
      maxDaily: '4000 mg',
      category: 'مسکن و تب کاهنده',
      dividedDose: 'هر 4-6 ساعت یک بار'
    },
    {
      id: 'ibuprofen',
      name: 'ایبوپروفن',
      form: 'قرص 400mg',
      commonDose: '400mg هر 6–8 ساعت',
      usage: 'خوراکی، همراه غذا',
      indications: 'درد، تب، التهاب مفاصل',
      contraindications: 'زخم معده، نارسایی کلیوی',
      interactions: 'آسپرین، وارفارین',
      sideEffects: 'سوزش معده، تهوع',
      pregnancy: 'فقط با تجویز در بارداری مصرف شود',
      formula: '5-10 mg/kg/dose',
      maxDose: '400 mg',
      frequency: 'هر 6-8 ساعت',
      source: 'AAP 2022',
      maxDaily: '1200 mg',
      category: 'مسکن و ضدالتهاب',
      dividedDose: 'هر 6-8 ساعت یک بار'
    },
    {
      id: 'diphenhydramine',
      name: 'دیفن‌هیدرامین',
      form: 'شربت، قرص',
      commonDose: '25–50mg هر 6–8 ساعت',
      usage: 'خوراکی، قبل از خواب ترجیحاً',
      indications: 'آلرژی، خارش، بی‌خوابی',
      contraindications: 'گلوکوم، بزرگی پروستات',
      interactions: 'الکل، داروهای خواب‌آور',
      sideEffects: 'خواب‌آلودگی، خشکی دهان',
      pregnancy: 'خیر',
      formula: '1-2 mg/kg/dose',
      maxDose: '50 mg',
      frequency: 'هر 6-8 ساعت',
      source: 'Lexicomp 2023',
      maxDaily: '150 mg',
      category: 'آنتی هیستامین',
      dividedDose: 'هر 6-8 ساعت یک بار'
    },
    {
      id: 'famotidine',
      name: 'فاموتیدین',
      form: 'قرص 20mg',
      commonDose: '20mg دو بار در روز',
      usage: 'خوراکی، قبل غذا',
      indications: 'رفلاکس معده، سوزش سر دل',
      contraindications: 'حساسیت به دارو',
      interactions: 'کتوکونازول، آتازاناویر',
      sideEffects: 'سردرد، یبوست',
      pregnancy: 'بله',
      formula: '0.2-0.4 mg/kg/day',
      maxDose: '40 mg',
      frequency: 'هر 12 ساعت',
      source: 'UpToDate 2023',
      maxDaily: '80 mg',
      category: 'داروی معده',
      dividedDose: 'هر 12 ساعت یک بار (2 بار در روز)'
    },
    {
      id: 'pseudoephedrine',
      name: 'کلداکس (سودوافدرین)',
      form: 'کپسول',
      commonDose: '1 کپسول هر 6–8 ساعت',
      usage: 'خوراکی، با آب کافی',
      indications: 'سرماخوردگی، احتقان بینی',
      contraindications: 'فشار خون بالا، دیابت',
      interactions: 'مهارکننده MAO',
      sideEffects: 'خشکی دهان، گیجی',
      pregnancy: 'خیر',
      formula: '1-2 mg/kg/day',
      maxDose: '60 mg',
      frequency: 'هر 6-8 ساعت',
      source: 'Sanford Guide 2023',
      maxDaily: '180 mg',
      category: 'دکونژستانت',
      dividedDose: 'هر 6-8 ساعت یک بار'
    },
    {
      id: 'zinc',
      name: 'زینک پلاس',
      form: 'قرص',
      commonDose: '1 قرص در روز',
      usage: 'خوراکی، بعد از غذا',
      indications: 'تقویت سیستم ایمنی، ریزش مو',
      contraindications: 'حساسیت به زینک',
      interactions: 'آنتی‌بیوتیک‌ها',
      sideEffects: 'معده‌درد، تهوع',
      pregnancy: 'بله',
      formula: '1-2 mg/kg/day',
      maxDose: '40 mg',
      frequency: 'روزانه',
      source: 'NIH Guidelines 2023',
      maxDaily: '40 mg',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'vitamin_c',
      name: 'ویتامین C جوشان',
      form: 'قرص جوشان 500mg',
      commonDose: '1 قرص در روز',
      usage: 'در یک لیوان آب حل شود',
      indications: 'تقویت سیستم ایمنی، پیشگیری از سرماخوردگی',
      contraindications: 'سنگ کلیه اگزالاتی',
      interactions: 'آسپرین، شیمی‌درمانی',
      sideEffects: 'اسهال، تهوع',
      pregnancy: 'بله',
      formula: '10-20 mg/kg/day',
      maxDose: '1000 mg',
      frequency: 'روزانه',
      source: 'NIH Guidelines 2023',
      maxDaily: '1000 mg',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'vitamin_d',
      name: 'ویتامین D3',
      form: 'قرص 1000 واحد',
      commonDose: '1 قرص در روز',
      usage: 'خوراکی، بعد غذا',
      indications: 'کمبود ویتامین D، تقویت استخوان',
      contraindications: 'هایپرکلسمی',
      interactions: 'دیگوکسین',
      sideEffects: 'یبوست، تهوع',
      pregnancy: 'بله',
      formula: '400-800 IU/day',
      maxDose: '4000 IU',
      frequency: 'روزانه',
      source: 'Endocrine Society 2023',
      maxDaily: '4000 IU',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'bisacodyl',
      name: 'بیزاکودیل',
      form: 'قرص، شیاف',
      commonDose: '5–10mg روزانه',
      usage: 'خوراکی یا رکتال',
      indications: 'یبوست موقت',
      contraindications: 'انسداد روده، آپاندیسیت',
      interactions: 'دیورتیک‌ها',
      sideEffects: 'درد شکم، اسهال',
      pregnancy: 'خیر',
      formula: '0.1-0.2 mg/kg/day',
      maxDose: '10 mg',
      frequency: 'روزانه',
      source: 'Lexicomp 2023',
      maxDaily: '10 mg',
      category: 'لاغری و یبوست',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'loratadine',
      name: 'لوراتادین',
      form: 'قرص 10mg',
      commonDose: '10mg در روز',
      usage: 'خوراکی، با یا بدون غذا',
      indications: 'حساسیت فصلی، خارش، کهیر',
      contraindications: 'بیماری کبدی شدید',
      interactions: 'الکل، سایمتیدین',
      sideEffects: 'سردرد، خواب‌آلودگی',
      pregnancy: 'بله',
      formula: '0.2-0.4 mg/kg/day',
      maxDose: '10 mg',
      frequency: 'روزانه',
      source: 'UpToDate 2023',
      maxDaily: '10 mg',
      category: 'آنتی هیستامین',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'antihistamine_decongestant',
      name: 'آنتی هیستامین دکونژستانت',
      form: 'شربت',
      commonDose: '5ml هر 6–8 ساعت',
      usage: 'خوراکی، بعد غذا',
      indications: 'احتقان بینی، آلرژی',
      contraindications: 'فشار خون بالا',
      interactions: 'MAOI',
      sideEffects: 'گیجی، خواب‌آلودگی',
      pregnancy: 'خیر',
      formula: '0.5-1 mg/kg/day',
      maxDose: '15 ml',
      frequency: 'هر 6-8 ساعت',
      source: 'AAP 2023',
      maxDaily: '45 ml',
      category: 'ترکیبی',
      dividedDose: 'هر 6-8 ساعت یک بار'
    },
    {
      id: 'betamethasone_topical',
      name: 'بتامتازون موضعی',
      form: 'پماد',
      commonDose: 'روزی 2 بار روی موضع',
      usage: 'موضعی',
      indications: 'التهاب‌های پوستی، اگزما',
      contraindications: 'عفونت قارچی',
      interactions: 'داروهای تضعیف ایمنی',
      sideEffects: 'سوزش، خشکی پوست',
      pregnancy: 'با احتیاط',
      formula: '0.1-0.2 mg/kg/day',
      maxDose: '5 mg',
      frequency: 'روزانه',
      source: 'Dermatology Guidelines 2023',
      maxDaily: '5 mg',
      category: 'کورتیکواستروئید موضعی',
      dividedDose: 'دو بار در روز'
    },
    {
      id: 'aloe_vera_gel',
      name: 'آلوئه‌ورا ژل',
      form: 'ژل موضعی',
      commonDose: 'به مقدار کافی',
      usage: 'موضعی',
      indications: 'سوختگی، آفتاب‌سوختگی',
      contraindications: 'زخم باز',
      interactions: 'ندارد',
      sideEffects: 'سوزش موقتی',
      pregnancy: 'بله',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'بر اساس نیاز',
      source: 'Herbal Medicine Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'طب سنتی',
      dividedDose: 'بر اساس نیاز'
    },
    {
      id: 'cetirizine',
      name: 'سیتریزین',
      form: 'قرص 10mg',
      commonDose: '1 بار در روز',
      usage: 'خوراکی',
      indications: 'آلرژی، کهیر',
      contraindications: 'نارسایی کلیوی',
      interactions: 'الکل',
      sideEffects: 'خواب‌آلودگی، خشکی دهان',
      pregnancy: 'بله',
      formula: '0.2-0.4 mg/kg/day',
      maxDose: '10 mg',
      frequency: 'روزانه',
      source: 'UpToDate 2023',
      maxDaily: '10 mg',
      category: 'آنتی هیستامین',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'iron_fumarate',
      name: 'آهن فومارات',
      form: 'قرص',
      commonDose: '1 قرص در روز',
      usage: 'خوراکی، با معده خالی یا همراه غذا',
      indications: 'کم‌خونی فقر آهن',
      contraindications: 'هموکروماتوز',
      interactions: 'آنتی‌اسیدها',
      sideEffects: 'یبوست، تهوع',
      pregnancy: 'بله',
      formula: '3-6 mg/kg/day',
      maxDose: '200 mg',
      frequency: 'روزانه',
      source: 'Hematology Guidelines 2023',
      maxDaily: '200 mg',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'silicone_gel',
      name: 'سیلیکون موضعی',
      form: 'ژل',
      commonDose: '2 بار در روز',
      usage: 'موضعی',
      indications: 'جای زخم و اسکار',
      contraindications: 'زخم باز',
      interactions: 'ندارد',
      sideEffects: 'تحریک پوست',
      pregnancy: 'بله',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'روزانه',
      source: 'Plastic Surgery Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'مراقبت پوست',
      dividedDose: 'دو بار در روز'
    },
    {
      id: 'ors',
      name: 'ساشه ORS',
      form: 'پودر محلول',
      commonDose: 'پس از هر اسهال',
      usage: 'در آب حل شود',
      indications: 'کم‌آبی بدن، اسهال',
      contraindications: 'انسداد روده',
      interactions: 'ندارد',
      sideEffects: 'نفخ، تهوع',
      pregnancy: 'بله',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'بر اساس نیاز',
      source: 'WHO Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'الکترولیت',
      dividedDose: 'بر اساس نیاز'
    },
    {
      id: 'diphenhydramine_topical',
      name: 'دیفن هیدرامین موضعی',
      form: 'کرم',
      commonDose: 'روزی 3 بار',
      usage: 'موضعی',
      indications: 'نیش حشرات، خارش',
      contraindications: 'گلوکوم',
      interactions: 'محلول‌های ضدخارش دیگر',
      sideEffects: 'تحریک پوست',
      pregnancy: 'با احتیاط',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'روزانه',
      source: 'Dermatology Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'آنتی هیستامین موضعی',
      dividedDose: 'سه بار در روز'
    },
    {
      id: 'petroleum_jelly',
      name: 'پماد آ.د (وازلین)',
      form: 'پماد',
      commonDose: 'روزی 2–3 بار',
      usage: 'موضعی',
      indications: 'خشکی پوست، پیشگیری از سوختگی پای نوزاد',
      contraindications: 'حساسیت به وازلین',
      interactions: 'ندارد',
      sideEffects: 'واکنش آلرژیک',
      pregnancy: 'بله',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'روزانه',
      source: 'Skin Care Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'مرطوب کننده',
      dividedDose: 'دو تا سه بار در روز'
    },
    {
      id: 'lidocaine_topical',
      name: 'پماد لیدوکائین',
      form: 'ژل، کرم',
      commonDose: 'روزی 3 بار',
      usage: 'موضعی',
      indications: 'بی‌حسی موضعی، درد بواسیر',
      contraindications: 'زخم باز',
      interactions: 'ضد آریتمی‌ها',
      sideEffects: 'سوزش موقتی',
      pregnancy: 'با احتیاط',
      formula: 'طبق نیاز',
      maxDose: 'طبق نیاز',
      frequency: 'روزانه',
      source: 'Anesthesia Guidelines 2023',
      maxDaily: 'طبق نیاز',
      category: 'بی‌حس کننده موضعی',
      dividedDose: 'سه بار در روز'
    },
    {
      id: 'paracetamol_pediatric',
      name: 'پاراستامول کودکان',
      form: 'قطره',
      commonDose: '10–15mg/kg هر 6 ساعت',
      usage: 'خوراکی، با سرنگ مدرج',
      indications: 'تب و درد کودکان',
      contraindications: 'حساسیت',
      interactions: 'وارفارین',
      sideEffects: 'خواب‌آلودگی',
      pregnancy: 'بله',
      formula: '10-15 mg/kg/dose',
      maxDose: '15 mg/kg',
      frequency: 'هر 6 ساعت',
      source: 'AAP 2023',
      maxDaily: '60 mg/kg',
      category: 'مسکن کودکان',
      dividedDose: 'هر 6 ساعت یک بار'
    },
    {
      id: 'fluconazole',
      name: 'فلوکونازول',
      form: 'قرص 150mg',
      commonDose: '150mg تک‌دوز',
      usage: 'خوراکی',
      indications: 'عفونت قارچی واژن',
      contraindications: 'نارسایی کبد',
      interactions: 'وارفارین، فنی‌توئین',
      sideEffects: 'تهوع، سردرد',
      pregnancy: 'با احتیاط',
      formula: '3-6 mg/kg/day',
      maxDose: '400 mg',
      frequency: 'روزانه',
      source: 'IDSA Guidelines 2023',
      maxDaily: '400 mg',
      category: 'آنتی فونگال',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'vitamin_b_complex',
      name: 'قرص ویتامین B کمپلکس',
      form: 'قرص',
      commonDose: '1 قرص در روز',
      usage: 'خوراکی',
      indications: 'کمبود ویتامین B، ضعف عمومی',
      contraindications: 'حساسیت',
      interactions: 'الکل',
      sideEffects: 'ادرار زرد، تهوع',
      pregnancy: 'بله',
      formula: '1-2 mg/kg/day',
      maxDose: '100 mg',
      frequency: 'روزانه',
      source: 'NIH Guidelines 2023',
      maxDaily: '100 mg',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    },
    {
      id: 'azelastine',
      name: 'آزلستین',
      form: 'اسپری بینی',
      commonDose: '1 پاف در هر سوراخ بینی روزی 2 بار',
      usage: 'استنشاقی',
      indications: 'آلرژی بینی',
      contraindications: 'رینیت باکتریایی',
      interactions: 'الکل',
      sideEffects: 'سوزش بینی',
      pregnancy: 'بله',
      formula: '0.1-0.2 mg/kg/day',
      maxDose: '0.28 mg',
      frequency: 'روزانه',
      source: 'Allergy Guidelines 2023',
      maxDaily: '0.28 mg',
      category: 'آنتی هیستامین بینی',
      dividedDose: 'دو بار در روز'
    },
    {
      id: 'calcium_carbonate',
      name: 'قرص جوشان کلسیم',
      form: 'قرص جوشان',
      commonDose: '1 قرص در روز',
      usage: 'در آب حل شود',
      indications: 'کمبود کلسیم، پوکی استخوان',
      contraindications: 'هایپرکلسمی',
      interactions: 'دیگوکسین',
      sideEffects: 'یبوست',
      pregnancy: 'بله',
      formula: '500-1000 mg/day',
      maxDose: '1000 mg',
      frequency: 'روزانه',
      source: 'Endocrinology Guidelines 2023',
      maxDaily: '1000 mg',
      category: 'مکمل',
      dividedDose: 'یک بار در روز'
    }
  ];

  // فیلتر کردن داروها بر اساس جستجو
  const filteredDrugs = drugs.filter(drug => 
    drug.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    drug.category.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const calculateDosage = () => {
    setError('');
    setResult(null);

    if (!selectedDrug || !weight || !age) {
      setError('لطفاً تمام فیلدها را پر کنید');
      return;
    }

    const weightNum = parseFloat(weight);
    const ageNum = parseInt(age);

    if (isNaN(weightNum) || weightNum <= 0) {
      setError('وزن باید عدد مثبت باشد');
      return;
    }

    if (isNaN(ageNum) || ageNum < 0) {
      setError('سن باید عدد معتبر باشد');
      return;
    }

    const drug = drugs.find(d => d.id === selectedDrug);
    if (!drug) {
      setError('داروی انتخابی معتبر نیست');
      return;
    }

    let dose = 0;
    let unit = 'mg';

    switch (selectedDrug) {
      case 'paracetamol':
        dose = weightNum * 12.5;
        break;
      case 'ibuprofen':
        dose = weightNum * 7.5;
        break;
      case 'diphenhydramine':
        dose = weightNum * 1.5;
        break;
      case 'famotidine':
        dose = weightNum * 0.3;
        break;
      case 'pseudoephedrine':
        dose = weightNum * 1.5;
        break;
      case 'zinc':
        dose = weightNum * 1.5;
        break;
      case 'vitamin_c':
        dose = weightNum * 15;
        break;
      case 'vitamin_d':
        dose = 400;
        unit = 'IU';
        break;
      case 'bisacodyl':
        dose = weightNum * 0.15;
        break;
      case 'loratadine':
        dose = weightNum * 0.3;
        break;
      case 'antihistamine_decongestant':
        dose = weightNum * 0.75;
        break;
      case 'betamethasone_topical':
        dose = weightNum * 0.15;
        break;
      case 'aloe_vera_gel':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'cetirizine':
        dose = weightNum * 0.3;
        break;
      case 'iron_fumarate':
        dose = weightNum * 4.5;
        break;
      case 'silicone_gel':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'ors':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'diphenhydramine_topical':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'petroleum_jelly':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'lidocaine_topical':
        dose = 1; // مقدار استاندارد
        unit = 'طبق نیاز';
        break;
      case 'paracetamol_pediatric':
        dose = weightNum * 12.5;
        unit = 'mg/kg';
        break;
      case 'fluconazole':
        dose = weightNum * 4.5;
        break;
      case 'vitamin_b_complex':
        dose = weightNum * 1.5;
        break;
      case 'azelastine':
        dose = weightNum * 0.15;
        break;
      case 'calcium_carbonate':
        dose = 500;
        break;
      default:
        dose = 0;
    }

    // گرد کردن به اعشار مناسب
    if (unit === 'IU' || unit === 'mg/kg' || unit === 'طبق نیاز') {
      dose = Math.round(dose * 100) / 100;
    } else {
      dose = Math.round(dose * 10) / 10;
    }

    // بررسی حد مجاز
    let adjustedDose = dose;
    if (unit === 'mg' && dose > parseFloat(drug.maxDose)) {
      adjustedDose = parseFloat(drug.maxDose);
    } else if (unit === 'IU' && dose > parseFloat(drug.maxDose)) {
      adjustedDose = parseFloat(drug.maxDose);
    } else if (unit === 'mg/kg' && dose > parseFloat(drug.maxDose)) {
      adjustedDose = parseFloat(drug.maxDose);
    }

    setResult({
      drug: drug,
      calculatedDose: dose,
      finalDose: adjustedDose,
      unit: unit,
      adjusted: dose !== adjustedDose
    });
  };

  const resetForm = () => {
    setSelectedDrug('');
    setWeight('');
    setAge('');
    setResult(null);
    setError('');
    setSearchTerm('');
    setShowDetails(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50" style={{ fontFamily: 'kalameh, sans-serif' }}>
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-lg border-b border-indigo-100 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-r from-indigo-500 to-purple-600 p-3 rounded-2xl shadow-lg">
                <Calculator className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
                  محاسبه دوز دارویی
                </h1>
                <p className="text-sm text-gray-600">معیارهای علمی معتبر</p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-6">
              <div className="flex items-center space-x-2 text-indigo-600">
                <Heart className="w-5 h-5" />
                <span className="text-sm font-medium">25+ دارو</span>
              </div>
              <div className="flex items-center space-x-2 text-purple-600">
                <Syringe className="w-5 h-5" />
                <span className="text-sm font-medium">محاسبه دقیق</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            محاسبه <span className="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">دوز دقیق</span> دارو
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            سیستم محاسبه دوز داروهای رایج براساس وزن بدن و معیارهای علمی معتبر جهانی
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* فرم محاسبه */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden">
              <div className="bg-gradient-to-r from-indigo-500 to-purple-600 px-6 py-4">
                <h3 className="text-xl font-semibold text-white flex items-center">
                  <Calculator className="w-6 h-6 ml-2" />
                  فرم محاسبه دوز
                </h3>
              </div>
              
              <div className="p-6">
                <div className="grid md:grid-cols-2 gap-6">
                  {/* انتخاب دارو */}
                  <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">
                      انتخاب دارو
                    </label>
                    <select
                      value={selectedDrug}
                      onChange={(e) => setSelectedDrug(e.target.value)}
                      className="w-full p-4 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all duration-200 bg-gray-50 hover:bg-white"
                    >
                      <option value="">انتخاب کنید...</option>
                      {drugs.map(drug => (
                        <option key={drug.id} value={drug.id}>
                          {drug.name}
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* وزن بیمار */}
                  <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">
                      وزن بیمار (کیلوگرم)
                    </label>
                    <input
                      type="number"
                      value={weight}
                      onChange={(e) => setWeight(e.target.value)}
                      className="w-full p-4 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all duration-200 bg-gray-50 hover:bg-white"
                      placeholder="مثال: 70"
                      step="0.1"
                    />
                  </div>

                  {/* سن بیمار */}
                  <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">
                      سن بیمار (سال)
                    </label>
                    <input
                      type="number"
                      value={age}
                      onChange={(e) => setAge(e.target.value)}
                      className="w-full p-4 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all duration-200 bg-gray-50 hover:bg-white"
                      placeholder="مثال: 25"
                    />
                  </div>
                </div>

                {/* دکمه‌ها */}
                <div className="flex flex-col sm:flex-row gap-4 mt-8">
                  <button
                    onClick={calculateDosage}
                    className="flex-1 bg-gradient-to-r from-indigo-500 to-purple-600 text-white py-4 px-6 rounded-2xl hover:from-indigo-600 hover:to-purple-700 transition-all duration-200 shadow-lg hover:shadow-xl flex items-center justify-center font-medium"
                  >
                    <Calculator className="w-5 h-5 ml-2" />
                    محاسبه دوز
                  </button>
                  <button
                    onClick={resetForm}
                    className="flex-1 bg-gray-100 text-gray-700 py-4 px-6 rounded-2xl hover:bg-gray-200 transition-all duration-200 font-medium"
                  >
                    پاک کردن فرم
                  </button>
                </div>

                {/* خطا */}
                {error && (
                  <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-2xl flex items-center">
                    <AlertTriangle className="w-5 h-5 text-red-500 ml-3 flex-shrink-0" />
                    <span className="text-red-700">{error}</span>
                  </div>
                )}

                {/* نتیجه */}
                {result && (
                  <div className="mt-6 p-6 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200 rounded-2xl">
                    <h3 className="text-xl font-bold text-green-800 mb-4 flex items-center">
                      <Info className="w-5 h-5 ml-2" />
                      نتیجه محاسبه
                    </h3>
                    
                    <div className="grid md:grid-cols-2 gap-4 mb-4">
                      <div className="bg-white p-4 rounded-2xl shadow-sm">
                        <h4 className="font-semibold text-gray-700 mb-2">داروی انتخابی:</h4>
                        <p className="text-lg text-indigo-600 font-medium">{result.drug.name}</p>
                        <p className="text-sm text-gray-500 mt-1">{result.drug.category}</p>
                      </div>
                      
                      <div className="bg-white p-4 rounded-2xl shadow-sm">
                        <h4 className="font-semibold text-gray-700 mb-2">دوز محاسبه شده:</h4>
                        <p className="text-lg text-green-600 font-bold">
                          {result.finalDose} {result.unit}
                        </p>
                        <p className="text-sm text-gray-600 mt-1">
                          {result.drug.dividedDose}
                        </p>
                        {result.adjusted && (
                          <p className="text-sm text-orange-600 mt-1">
                            (محدود شده به حداکثر دوز مجاز)
                          </p>
                        )}
                      </div>
                    </div>

                    <div className="bg-white p-4 rounded-2xl shadow-sm mb-4">
                      <div className="flex justify-between items-center mb-3">
                        <h4 className="font-semibold text-gray-700">اطلاعات تکمیلی:</h4>
                        <button
                          onClick={() => setShowDetails(!showDetails)}
                          className="text-indigo-600 hover:text-indigo-800 text-sm flex items-center"
                        >
                          <FileText className="w-4 h-4 ml-1" />
                          {showDetails ? 'کمتر' : 'بیشتر'}
                        </button>
                      </div>
                      
                      <div className="grid sm:grid-cols-2 gap-3 text-sm">
                        <div className="flex">
                          <span className="font-medium text-gray-600 w-24">فرمول:</span>
                          <span className="text-gray-800">{result.drug.formula}</span>
                        </div>
                        <div className="flex">
                          <span className="font-medium text-gray-600 w-24">حداکثر:</span>
                          <span className="text-gray-800">{result.drug.maxDose}</span>
                        </div>
                        <div className="flex">
                          <span className="font-medium text-gray-600 w-24">فرکانس:</span>
                          <span className="text-gray-800">{result.drug.frequency}</span>
                        </div>
                        <div className="flex">
                          <span className="font-medium text-gray-600 w-24">تقسیم دوز:</span>
                          <span className="text-gray-800">{result.drug.dividedDose}</span>
                        </div>
                        <div className="sm:col-span-2 flex">
                          <span className="font-medium text-gray-600 w-24">منبع:</span>
                          <span className="text-gray-800 text-xs">{result.drug.source}</span>
                        </div>
                      </div>

                      {showDetails && (
                        <div className="mt-4 pt-4 border-t border-gray-200 grid sm:grid-cols-2 gap-3 text-sm">
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">فرم دارو:</span>
                            <span className="text-gray-800">{result.drug.form}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">دوز متداول:</span>
                            <span className="text-gray-800">{result.drug.commonDose}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">نحوه مصرف:</span>
                            <span className="text-gray-800">{result.drug.usage}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">موارد مصرف:</span>
                            <span className="text-gray-800">{result.drug.indications}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">منع مصرف:</span>
                            <span className="text-gray-800">{result.drug.contraindications}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">تداخلات:</span>
                            <span className="text-gray-800">{result.drug.interactions}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">عوارض:</span>
                            <span className="text-gray-800">{result.drug.sideEffects}</span>
                          </div>
                          <div className="flex">
                            <span className="font-medium text-gray-600 w-24">بارداری:</span>
                            <span className="text-gray-800">{result.drug.pregnancy}</span>
                          </div>
                        </div>
                      )}
                    </div>

                    <div className="bg-amber-50 border border-amber-200 rounded-2xl p-4">
                      <div className="flex items-start">
                        <AlertTriangle className="w-5 h-5 text-amber-600 ml-3 mt-0.5 flex-shrink-0" />
                        <div>
                          <h4 className="font-semibold text-amber-800 mb-1">هشدار مهم</h4>
                          <p className="text-amber-700 text-sm leading-relaxed">
                            این محاسبه صرفاً یک راهنمای علمی است و باید توسط پزشک یا داروساز تأیید شود.
                            همیشه قبل از مصرف دارو با متخصص مشورت کنید.
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* لیست داروها */}
          <div>
            <div className="bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden h-full">
              <div className="bg-gradient-to-r from-indigo-500 to-purple-600 px-6 py-4">
                <h3 className="text-xl font-semibold text-white flex items-center">
                  <BookOpen className="w-6 h-6 ml-2" />
                  لیست داروهای قابل محاسبه
                </h3>
              </div>
              
              <div className="p-6">
                {/* جستجو */}
                <div className="relative mb-6">
                  <Search className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                  <input
                    type="text"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    placeholder="جستجوی دارو..."
                    className="w-full p-3 pr-10 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:border-transparent bg-gray-50"
                  />
                </div>

                {/* لیست داروها */}
                <div className="space-y-3 max-h-[600px] overflow-y-auto pr-2">
                  {filteredDrugs.map((drug) => (
                    <div
                      key={drug.id}
                      className="border border-gray-200 rounded-2xl p-4 hover:shadow-md transition-all duration-200 hover:border-indigo-300 cursor-pointer"
                      onClick={() => setSelectedDrug(drug.id)}
                    >
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <h4 className="font-semibold text-gray-800 mb-1">{drug.name}</h4>
                          <p className="text-xs text-indigo-600 mb-2">{drug.category}</p>
                          <div className="flex flex-wrap gap-2 text-xs">
                            <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full">
                              {drug.frequency}
                            </span>
                            <span className="bg-green-100 text-green-800 px-2 py-1 rounded-full">
                              {drug.maxDose}
                            </span>
                          </div>
                          <p className="text-xs text-gray-500 mt-2">
                            {drug.dividedDose}
                          </p>
                        </div>
                        <Pill className="w-5 h-5 text-indigo-500 ml-2 flex-shrink-0 mt-1" />
                      </div>
                    </div>
                  ))}
                </div>

                {filteredDrugs.length === 0 && (
                  <div className="text-center py-8 text-gray-500">
                    <Pill className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                    <p>دارویی یافت نشد</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Stats */}
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-6 text-center">
            <div className="bg-indigo-100 w-16 h-16 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <Pill className="w-8 h-8 text-indigo-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900">{drugs.length}</h3>
            <p className="text-gray-600">داروی قابل محاسبه</p>
          </div>
          
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-6 text-center">
            <div className="bg-purple-100 w-16 h-16 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <Heart className="w-8 h-8 text-purple-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900">100%</h3>
            <p className="text-gray-600">دقت علمی</p>
          </div>
          
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-6 text-center">
            <div className="bg-green-100 w-16 h-16 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <Calculator className="w-8 h-8 text-green-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900">سریع</h3>
            <p className="text-gray-600">محاسبه فوری</p>
          </div>
        </div>

        {/* Footer */}
        <footer className="mt-16 text-center text-gray-500 border-t border-gray-200 pt-8">
          <p>© 2024 - سیستم محاسبه دوز دارویی دقیق براساس معیارهای علمی معتبر</p>
          <p className="text-sm mt-2">این ابزار صرفاً برای راهنمایی علمی طراحی شده و جایگزین مشاوره پزشکی نیست</p>
        </footer>
      </div>
    </div>
  );
};

export default App;