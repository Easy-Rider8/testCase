import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 100 },  // 30 saniyede 100 kullanıcıya çık
    { duration: '1m', target: 500 },   // 1 dakika boyunca 500 kullanıcıda kal
    { duration: '30s', target: 0 }     // 30 saniyede yükü sıfırlama
  ],
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/users');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is below 1s': (r) => r.timings.duration < 1000,
  });
  sleep(1);
}
