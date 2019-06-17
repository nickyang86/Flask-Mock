import request from '@/utils/request'

export function test() {
  return request({
    url: '/general/test',
    method: 'get'
  })
}
