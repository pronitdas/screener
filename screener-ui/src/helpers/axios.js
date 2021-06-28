const axios = require('axios');

const instance = axios.create({
    baseURL: 'https://some-domain.com/api/',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
  });


module.exports = {
    axiosInstance: instance
}