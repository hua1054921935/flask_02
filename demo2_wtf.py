# coding=utf-8
# coding=utf-8

from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
# 导入wtforms提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
# 解决编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
app.secret_key='heima'

@app.route('/')
def hello_world():

    return 'hello flask'

@app.route('/demo_wtf', methods=['GET', 'POST'])
def demo_wtf():
    # 判断请求方式
    if request.method=='POST':

        # 获取参数
        username=request.form.get('username')
        password=request.form.get('password')
        password2 = request.form.get('password2')

        # 参数校验
        if not all([username,password,password2]):
            flash(u'参数不完整')
            print username,password
        elif password!=password2:
            flash(u'密码不一致')
        else:
            print username
            return 'success'



        # 业务处理
        # 返回应答

    return render_template('demo2_wtf.html')

# 自定义表单名
class LoginForm(FlaskForm):

    username=StringField('用户名:',validators=[DataRequired()],render_kw={'placeholder': '请输入用户名'})
    password=PasswordField('密码:',validators=[DataRequired()],render_kw={'placeholder': '请输入密码'})
    password2 = PasswordField('确认密码:',validators=[DataRequired(),EqualTo('password','输入密码不一致')],render_kw={'placeholder': '确认密码'})
    submit=SubmitField('提交')

@app.route('/form',methods=['GET','POST'])
def form():
    # login=LoginForm()
    # if request.method=='POST':
    #     if login.validate_on_submit():
    #         return 'success'
    #     else:
    #         messages=login.errors
    #         flash(messages)
    #         # 3. 验证成功 获取参数 --> request.form
    # 1. 需要判断请求方式为POST\
    login_form = LoginForm()
    if request.method == 'POST':

        # 2. 校验参数 (完整性 & 判断密码是否相同)
        # validate_on_submit: 在点击提交时进行验证. 验证的要求在前面已经指定了. 这里会把所有的验证全部执行
        if login_form.validate_on_submit():

            # 3. 验证成功 获取参数 --> request.form
            # username = request.form.get('username')
            # password = request.form.get('password')
            # password2 = request.form.get('password2')

            # 4. 如果都正确, 返回success
            return 'success'
        else:
            # 表单出的错误, 都在login_form.errors里面
            # message = login_form.errors.get('password2')[0]
            message = login_form.errors
            flash(message)
            # flash('验证不通过')


    return render_template('demo2_wtf.html',form=login_form)


if __name__ == '__main__':
    app.run(debug=True)