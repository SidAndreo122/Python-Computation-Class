class Form_X:
    def __init__(self, f_name):
        self._f_name = f_name

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self, new_f_name):
        if not isinstance(new_f_name, str):
            raise ValueError("first name must be a string.")

        self._f_name = new_f_name

Form_X = Form_X("Sabine")

print(Form_X.f_name)   

Form_X.f_name = 2187

print(Form_X.f_name)   
