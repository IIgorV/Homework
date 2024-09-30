immutable_var_ = 1,2,3,4, 'Text', False
print(immutable_var_)
immutable_var_[0]
print(immutable_var_[0])
immutable_var_[0] = 200
print(immutable_var_)

mutable_list_ = ([1, 2], 'is', True, 1, "Money")
print(mutable_list_)
mutable_list_[0][0] = 'Sun'
print(mutable_list_)