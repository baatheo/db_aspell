let mix = require('laravel-mix');

mix
    .options({
        processCssUrls: false,
    })
    .disableSuccessNotifications()
    .sourceMaps(false, 'source-map')
    .sass('front/scss/app.scss', 'flaskr/static/app.css')
    .js('front/js/app.js', 'flaskr/static/app.js');

