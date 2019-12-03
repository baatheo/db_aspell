let mix = require('laravel-mix');

mix
    .disableSuccessNotifications()
    .options({
        processCssUrls: false,
    })
    .sourceMaps(false, 'source-map')
    .sass('front/scss/app.scss', 'flaskr/static/app.css')
    .js('front/js/app.js', 'flaskr/static/app.js')
    .copyDirectory("node_modules/@fortawesome/fontawesome-free/webfonts", "flaskr/static/webfonts");

