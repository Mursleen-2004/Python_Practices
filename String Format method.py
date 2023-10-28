# format(): data ko format krta ha. ye hume option deta ha ky hum koi bhi value string ky darmiyan me insert kr skty hain
#  {} ye indicate krta ha ky isme run-time pe koi value insert hony wali ha.

a = "my name is musa."
print(a);
a = "my name is {name}".format(name="irfan");
print(a);