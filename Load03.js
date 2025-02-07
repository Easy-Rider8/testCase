import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1h', target: 100 },   // 1 saat boyunca 100 kullanıcıda kal
    { duration: '1h', target: 100 },   // 1 saat boyunca 100 kullanıcıda kal
    { duration: '30s', target: 0 }     // 30 saniyede yükü sıfırlama
  ],
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/users');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is below 2s': (r) => r.timings.duration < 2000,
  });
  sleep(1);
}
