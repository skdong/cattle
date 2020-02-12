package tools

func Tasks() {
	packages := make([]int, 24*1024*1024)
	for i := 0; i < 24*1024*1024; i++ {
		packages[i] = i
	}
}
