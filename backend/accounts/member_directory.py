import re


PUBLIC_MEMBER_EXCLUDED_NAMES = {
    "احمد",
    "دکتر امیر رضائی",
    "دکتر بابک قالیباف",
    "دکتر حسینعلی غفاری پور",
    "دکتر ذلفا مدرسی",
    "دکتر روح الله شیرزادی",
    "دکتر سهیلا خلیل زاده",
    "دکتر سید احمد طباطبائی",
    "دکتر سید جواد سیدی",
    "دکتر سید حسین میر لوحی",
    "دکتر سید محمد رضا میرکریمی",
    "دکتر علیرضا اسدی",
    "دکتر علیرضا عشقی",
    "دکتر قرم تاج خان بابایی",
    "دکتر لعبت شاهکار",
    "دکتر مجید کیوانفر",
    "دکتر محسن علی سمیر",
    "دکتر محمد رضا مدرسی",
    "دکتر محمد رضائی",
    "دکتر معصومه قاسمپور علمداری",
    "دکتر نازنین فرحبخش",
    "زهرا",
    "علی",
    "فاطمه",
    "محمد",
}

FIRST_NAME_OVERRIDES = {
    ".mohammadreza modaresi": "محمدرضا مدرسی",
    "Elhamsadati": "الهام ساداتی",
    "MD. Ali": "علی",
    "Mohammmad Rezaei": "محمد رضائی",
    "Nooshin.Baghaie": "نوشین بقایی",
}


def contains_latin(value: str) -> bool:
    return bool(re.search(r"[A-Za-z]", value or ""))


def contains_persian(value: str) -> bool:
    return bool(re.search(r"[\u0600-\u06FF]", value or ""))


def cleaned_name(value: str) -> str:
    return " ".join((value or "").strip().split())


def candidate_public_names(user) -> set[str]:
    names = {
        cleaned_name(getattr(user, "first_name", "")),
        cleaned_name(getattr(user, "last_name", "")),
        cleaned_name(f"{getattr(user, 'first_name', '')} {getattr(user, 'last_name', '')}"),
    }
    return {name for name in names if name}


def should_hide_from_public_members(user) -> bool:
    if getattr(user, "is_superuser", False):
        return True

    username = getattr(user, "username", "") or ""
    if username.startswith("system_import") or username.startswith("board_"):
        return True

    return bool(candidate_public_names(user) & PUBLIC_MEMBER_EXCLUDED_NAMES)


def preferred_persian_name(user) -> str:
    first_name = cleaned_name(getattr(user, "first_name", ""))
    last_name = cleaned_name(getattr(user, "last_name", ""))

    if first_name in FIRST_NAME_OVERRIDES:
        return FIRST_NAME_OVERRIDES[first_name]
    if contains_latin(first_name) and contains_persian(last_name):
        return last_name
    if contains_persian(first_name):
        return first_name
    if contains_persian(last_name):
        return last_name
    return first_name or last_name
