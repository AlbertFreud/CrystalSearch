sin,cos,sqrt=math.sin,math.cos,math.sqrt
pow,exp=math.pow,math.exp
rand=math.random

--[[
function render(t)
	glColor3d(1,1,1)
	glBegin(GL_LINE_STRIP)
	for x=-1,1,0.002 do
		--y=sin(x*50)*cos(x*10*(sin(t*0.4)*0.5+0.5)+t*2)
		--y=1/(1+x*x*10)*sin(x*50+t)
		--y=exp(-x^2*10)*sin(t+x*100)^2
		glVertex3d(x,y,0)
	end
	glEnd()
end
]]

function wavez(x,y,t)
	local r=sqrt(x*x+y*y)
	return 0.3*cos(r*10-t)*exp(-r*3)
end
function texcd(x,y,t)
	return x*0.5+0.5,y*0.5+0.5
end
function norm(x,y,t)
	local dd=0.0001
	local nx=-(wavez(x+dd,y,t)-wavez(x,y,t))/dd
	local ny=-(wavez(x,y+dd,t)-wavez(x,y,t))/dd
	local nz=1
	local nr=sqrt(nx^2+ny^2+nz^2)
	return nx/nr,ny/nr,nz/nr
	--return 0,0,1
end
function render(t)
	local dx,dy=0.1,0.1 
	glColor3d(1,1,1)
	for y=-1,1-dy,dy do
		glBegin(GL_QUAD_STRIP)
		for x=-1,1,dx do
            glTexCoord2d(texcd(x,y+dy,t))
			glNormal3d(norm(x,y+dy,t));
			glVertex3d(x,y+dy,wavez(x,y+dy,t))
			
			glTexCoord2d(texcd(x,y,t))
			glNormal3d(norm(x,y,t));
			glVertex3d(x,y,wavez(x,y,t))
		end
		glEnd()
	end
end
