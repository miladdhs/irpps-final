# راهنمای پوشش متن در Django Template (Server-Side Rendering)

حالا فرانت‌اند به حالت Server-Side Rendering برگشته است. شما می‌توانید محتوا را مستقیماً در Django template پوشش دهید.

## ساختار فعلی

### 1. View Function (`backend/ispp_project/urls.py`)

```python
def spa_view(request):
    """Render SPA with server-side content"""
    context = {
        'page_title': 'انجمن علمی ریه کودکان',
        'page_description': 'مرکز تخصصی تحقیقات و درمان بیماری‌های ریوی کودکان',
        # Add more server-side content here that you want to mask/override
    }
    return render(request, 'index.html', context)
```

### 2. Template (`backend/templates/index.html`)

Template از Django context variables استفاده می‌کند:

```django
<title>{{ page_title|default:"انجمن علمی ریه کودکان" }}</title>
<meta name="description" content="{{ page_description|default:'...' }}">
```

## نحوه پوشش متن‌ها

### روش 1: اضافه کردن به Context در View

در فایل `backend/ispp_project/urls.py`، به `context` dictionary اضافه کنید:

```python
def spa_view(request):
    context = {
        'page_title': 'انجمن علمی ریه کودکان',
        'page_description': 'مرکز تخصصی تحقیقات و درمان بیماری‌های ریوی کودکان',
        
        # مثال: پوشش متن‌های اضافی
        'home_title': 'متن پوشیده شده برای صفحه اصلی',
        'home_subtitle': 'زیرعنوان پوشیده شده',
        'hero_description': 'توضیحات پوشیده شده',
        
        # می‌توانید از دیتابیس یا API هم استفاده کنید
        # 'dynamic_content': get_dynamic_content(request),
    }
    return render(request, 'index.html', context)
```

### روش 2: استفاده در Template

در `backend/templates/index.html`، از متغیرها استفاده کنید:

```django
{# در بخش head #}
<title>{{ page_title|default:"انجمن علمی ریه کودکان" }}</title>
<meta name="description" content="{{ page_description|default:'...' }}">

{# در بخش body (قبل از Vue mount) #}
<div id="app">
    <noscript>
        <div style="padding: 2rem; text-align: center;">
            <h1>{{ home_title|default:"انجمن علمی ریه کودکان" }}</h1>
            <p>{{ home_subtitle|default:"مرکز تخصصی..." }}</p>
            <p>{{ hero_description|default:"توضیحات..." }}</p>
        </div>
    </noscript>
</div>

{# انتقال داده به Vue از طریق JSON #}
<script id="ssr-data" type="application/json">
{
    "pageTitle": "{{ page_title|escapejs }}",
    "pageDescription": "{{ page_description|escapejs }}",
    "homeTitle": "{{ home_title|default:''|escapejs }}",
    "homeSubtitle": "{{ home_subtitle|default:''|escapejs }}"
}
</script>
```

### روش 3: استفاده از داده‌های دینامیک

می‌توانید از دیتابیس یا API استفاده کنید:

```python
from news.models import News
from events.models import Event

def spa_view(request):
    # مثال: دریافت اخبار
    latest_news = News.objects.filter(is_published=True)[:5]
    
    # مثال: دریافت رویدادها
    upcoming_events = Event.objects.filter(is_published=True)[:3]
    
    context = {
        'page_title': 'انجمن علمی ریه کودکان',
        'page_description': 'مرکز تخصصی تحقیقات و درمان بیماری‌های ریوی کودکان',
        'latest_news': latest_news,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'index.html', context)
```

سپس در template:

```django
{% for news_item in latest_news %}
    <div>
        <h3>{{ news_item.title }}</h3>
        <p>{{ news_item.short_content|truncatewords:30 }}</p>
    </div>
{% endfor %}
```

## نکات مهم

1. **Escape JS**: همیشه از `|escapejs` برای داده‌های JSON استفاده کنید
2. **Default Values**: از `|default:"..."` برای مقادیر پیش‌فرض استفاده کنید
3. **Performance**: برای داده‌های سنگین از caching استفاده کنید
4. **SEO**: محتوای مهم را در template قرار دهید تا برای SEO بهتر باشد

## مثال کامل

```python
# urls.py
def spa_view(request):
    context = {
        'page_title': 'انجمن علمی ریه کودکان',
        'page_description': 'مرکز تخصصی تحقیقات و درمان بیماری‌های ریوی کودکان',
        'home_badge': 'مراقبت پیشرفته تنفس کودکان',
        'home_title': 'انجمن علمی ریه کودکان',
        'home_subtitle': 'مرکز تخصصی تحقیقات و درمان بیماری‌های ریوی کودکان',
        'home_description': 'با جدیدترین رویکردهای علمی، تیم ما کنار خانواده‌ها و کودکان است',
    }
    return render(request, 'index.html', context)
```

```django
{# index.html #}
<title>{{ page_title }}</title>
<meta name="description" content="{{ page_description }}">

<script id="ssr-data" type="application/json">
{
    "home": {
        "badge": "{{ home_badge|escapejs }}",
        "title": "{{ home_title|escapejs }}",
        "subtitle": "{{ home_subtitle|escapejs }}",
        "description": "{{ home_description|escapejs }}"
    }
}
</script>
```

## استفاده در Vue.js

در Vue component، می‌توانید داده‌های SSR را بخوانید:

```javascript
// در main.ts یا App.vue
const ssrDataElement = document.getElementById('ssr-data');
if (ssrDataElement) {
    const ssrData = JSON.parse(ssrDataElement.textContent);
    // استفاده از ssrData در Vue app
    console.log(ssrData.pageTitle);
}
```

## به‌روزرسانی Template بعد از Build

بعد از `npm run build:prod`، فایل `update_template.py` به صورت خودکار template را به‌روزرسانی می‌کند، اما محتوای Django template tags (مثل `{% load static %}`) حفظ می‌شود.

**نکته**: بعد از build، اگر تغییرات در template دادید، دوباره template را بررسی کنید.

