const path = require('path');
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    mode: 'development',
    entry: {
        imageswitcher: './frontend/imageswitcher.js'
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
    ],
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'main/static/bundles')
    },
    module: {
        rules:[
            {
                test:/\.(js|jsx)$/,
                exclude:/(node_modules|bower_components)/,
                loader:"babel-loader",
                options:{ presets:["@babel/env"]}
            },
            {
                test:/\.css$/,
                use:["style-loader", "css-loader"]
            }
        ]
    },
    resolve:{extensions:["*", ".js", ".jsx"]},
};