#!/usr/bin/env python
# -*- coding: utf-8 -*-
#入门： https://segmentfault.com/a/1190000002965620
#进阶： http://python.jobbole.com/83922/
import unittest
import mock
import client

class TestClient(unittest.TestCase):
    '''
            找到要替换的对象：我们需要测试的是visit_ustack这个函数，那么我们需要替换掉send_request这个函数。
            实例化Mock类得到一个mock对象，并且设置这个mock对象的行为。在成功测试中，我们设置mock对象的返回值
            为字符串“200”，在失败测试中，我们设置mock对象的返回值为字符串"404"。
            使用这个mock对象替换掉我们想替换的对象。我们替换掉了client.send_request
            写测试代码。我们调用client.visit_ustack()，并且期望它的返回值和我们预设的一样。
    
    '''
    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_ustack(), '404')

class TestClientPatch(unittest.TestCase):
    '''
    patch返回一个mock内部的类实例，这个类是class _patch。返回的这个类实例
            既可以作为函数的装饰器，也可以作为类的装饰器，也可以作为上下文管理器。
            使用patch或者patch.object的目的是为了控制mock的范围，意思就是在一个
            函数范围内，或者一个类的范围内，或者with语句的范围内mock掉一个对象
    '''
    def test_success_request(self):
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        with mock.patch('client.send_request', success_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

    def test_fail_request(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('client.send_request', fail_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)
    
    '''
    patch用于装饰器,该方法使用起来比较简单易读：将client.send_request patch阻挡下来，
         模拟一个返回值为mock.Mock(return_value='200')
    '''
    @mock.patch('client.send_request', mock.Mock(return_value='200'))        
    def test_success_request(self):
        status_code = '200'
        from client import visit_ustack
        self.assertEqual(visit_ustack(), status_code)
            
class TestClientArgs(unittest.TestCase):
    '''
    Mock对象的call_args表示该mock对象被调用的tuple，tuple的每个成员都是
            一个mock.call对象。mock.call这个对象代表了一次对mock对象的调用，
            其内容是一个tuple，含有两个元素，第一个元素是调用mock对象时的位置
            参数（*args），第二个元素是调用mock对象时的关键字参数（**kwargs）。
    '''

    def test_call_send_request_with_right_arguments(self):
        client.send_request = mock.Mock()
        client.visit_ustack()
        self.assertEqual(client.send_request.called, True)
        call_args = client.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)


        