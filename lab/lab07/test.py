def add(s,v):
    assert s is not List.empty
    if s.first > v:
        s.frist,s.rest = link(v),s
    elif s.first < v and empty(s.rest):
        s.rest = link(v)
    elif s.first < v:
        
