a=float(input("请输入您的身高(m),例如1.80m   "))
b =float(input("请输入您的体重(kg),例如60kg   "))
BMI=b/(a**2)
if  18.5<=BMI<24:
    print(f"您的身材非常健康,BMI指数为{BMI:.1f}")    
else:  print("您的体重不健康")
if BMI<18.5:
    print(f"体重过轻,BMI指数为{BMI:.1f}")
elif BMI >=24:
    print(f"体重超标,BMI指数为{BMI:.1f}")
elif BMI>=27:
    print(f"体重过重,已属于肥胖。BMI指数为{BMI :.1f}")