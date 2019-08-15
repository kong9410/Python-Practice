"""
이코드는 트레이닝 진행사항을 나타내주는 코드입니다.
"""
class ProgBar():
    def __init__(self, step=100):
        self.step = int(step/20)
	self.count = 1
	self.progress = 0

    def update(self):
    	if self.count % self.step == 0:
	    self.progress += 1
	    print('\r[%s%s]' %('#'*self.progress, ' '*(20-self.progress)), end='')
	self.count += 1

