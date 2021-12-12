const { createProxyMiddleware } = require('http-proxy-middleware')

module.exports = function(app) {
    app.use('/login', createProxyMiddleware({ target: 'http://localhost:3001', changeOrigin: true })),
    app.use('/refresh', createProxyMiddleware({ target: 'http://localhost:3001', changeOrigin: true })),
    app.use('/recommend', createProxyMiddleware({ target: 'https://spotify-recommender-server.herokuapp.com', changeOrigin: true }))
}