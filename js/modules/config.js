export const CONFIG = {
    CHANNEL_NAME: 'roneer_', // Имя канала на Twitch
    TILT_FORCE: 3,
    ACHIEVEMENT_MAX_STACK: 3,
    ACHIEVEMENT_TIME: 4000,
    REDIRECT_DELAY: 1500,
    
    // База данных Roneer
    SUPABASE_URL: 'https://fuqttyjuqxamrzplhojh.supabase.co', 
    SUPABASE_KEY: 'sb_publishable_DxFq95NHfBhNjBXZLYLCuQ_fdaG4iHm',

    MAIN_SITE_URL: 'https://taplink.cc/roneer',
    GAMES_SITE_URL: '' 
};

export const ALLOWED_HOSTS =[
    "localhost",
    "127.0.0.1",
    "taplink.cc" // Добавим для тестов
];

export const ACHIEVEMENT_DATA = {
    'twitch':     { title: "Зашёл? Оставайся",          desc: "Открыл Twitch-канал" },
    'telegram':   { title: "Новости и уют",             desc: "Залетел в Telegram" },
    'youtube':    { title: "Архивариус",                desc: "Открыл YouTube" },
    'tiktok':     { title: "Зумерские приколы",         desc: "Зашел в TikTok" },
    'insta':      { title: "Личная жизнь",              desc: "Открыл Instagram" },
    'da':         { title: "Пенсионный фонд",           desc: "Закинул донат на базу" },
    'ma':         { title: "Мемный магнат",             desc: "Отправил мем на стрим" },
    'qr-card':    { title: "Сканер",                    desc: "Отсканировал QR-код" },
    'autoclicker':{ title: "Куда жмёшь?!",              desc: "Сломал мышку об аватарку" },
    'click-67':   { title: "Разминка для пальцев",      desc: "67 кликов" },
    'click-100':  { title: "Сотня пробита",             desc: "100 кликов" },
    'click-228':  { title: "FPS Геймер",                desc: "228 кликов" },
    'click-666':  { title: "Адский аим",                desc: "666 кликов" },
    'click-777':  { title: "Джекпот",                   desc: "777 кликов" },
    'click-1000': { title: "Может, найдешь хобби?",     desc: "1000 кликов" },
    'click-1337': { title: "Киберспортсмен",            desc: "1337 кликов" },
    'click-1488': { title: "Пасхалочка",                desc: "1488 кликов" }
};