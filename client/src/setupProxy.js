const { createProxyMiddleware } = require('http-proxy-middleware')

module.exports = function(app) {
    app.use('/authServer', createProxyMiddleware({ target: 'http://localhost:3001', changeOrigin: true })),
    app.use('/recommenderServer', createProxyMiddleware({ target: 'http://localhost:3002', changeOrigin: true }))
}