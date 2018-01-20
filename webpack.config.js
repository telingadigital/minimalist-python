var ExtractTextPlugin = require('extract-text-webpack-plugin');
var path = require('path');

module.exports = {
	entry: './index.js',
	output: {
		path: path.resolve(__dirname, 'bundle'),
		filename: 'app.js'
	},
	module: {
		loaders: [
			{
				test: /\.js/,
				loader:'babel-loader',
			},
			{
				test: /\.css/,
				loader: ExtractTextPlugin.extract('css-loader'),
			}
		]
	},
	plugins: [
		new ExtractTextPlugin("app.css")
	]
}