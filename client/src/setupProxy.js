const { createProxyMiddleware } = require('http-proxy-middleware')

module.exports = function(app) {
    app.use('/authServer', createProxyMiddleware({ target: 'https://spotify-recommender-ejrp.herokuapp.com:3001', changeOrigin: true })),
    app.use('/recommenderServer', createProxyMiddleware({ target: 'https://spotify-recommender-server.herokuapp.com', changeOrigin: true }))
}