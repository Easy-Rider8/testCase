import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 50 },  // 30 saniyede 50 kullanıcıya çık
    { duration: '1m', target: 50 },   // 1 dakika boyunca 50 kullanıcıda kal
    { duration: '30s', target: 0 }    // 30 saniyede yükü düşür
  ],
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/users');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is below 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
