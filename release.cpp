#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <complex>
#include <string>
#include <time.h>

using namespace std;

int main(int argc, char* argv[]){

	complex <double> z;
	string model = "mandelbrot";
	complex <double> constant(0, 0.8);
	int threshold = 2;
	int limit = 1000;
	int width = 1000;
	int height = 800;
	double zoom = 0.6;
	int color = 9;
	bool no_show = false;
	string output = "no_path";
	bool exec_time = false;

	for (int i=1; i<argc; i++){
		if (string(argv[i]) == "-m"){
			model = string(argv[i + 1]);
			if ((model != "mandelbrot") && (model != "julia")){
				cout << "\nModel not found! Available models: mandelbrot, julia.\n";
				return -1;
			}
		}
		else if (model == "julia" && string(argv[i]) == "-c"){
			constant.real(atof(argv[i + 1]));
			constant.imag(atof(argv[i + 2]));
		}
		else if (string(argv[i]) == "-t") threshold = atoi(argv[i + 1]);
		else if (string(argv[i]) == "-l") limit = atoi(argv[i + 1]);
		else if (string(argv[i]) == "-s"){
			width = atoi(argv[i + 1]);
			height = atoi(argv[i + 2]);
		}
		else if (string(argv[i]) == "-z") zoom = atof(argv[i + 1]);
		else if (string(argv[i]) == "-r") color = atoi(argv[i + 1]);
		else if (string(argv[i]) == "-v") no_show = true;
		else if (string(argv[i]) == "-o") output = string(argv[i + 1]);
		else if (string(argv[i]) == "-i") exec_time = true;
	}
	clock_t t0 = clock();
	cv::Mat img(height, width, CV_32S);
	double re, im;
	int intensity;

	for (int i=0; i<width; i++){
		re = (i - (width * 0.5)) / (0.5 * width * zoom);
		for (int j=0; j<height; j++){
			im = -(j - (height * 0.5)) / (0.5 * height * zoom);
			z.real(re);
			z.imag(im);
			if (model == "mandelbrot") constant = z;
			intensity = 0;
			while ((abs(z) < threshold) && (intensity < limit)){
				z = z * z + constant;
				intensity++;
			}
			img.at<int>(j, i) = intensity;
		}
	}

	img.convertTo(img, CV_8U);
	cv::applyColorMap(img, img, color);

	if (exec_time)	cout << double(clock() - t0)/CLOCKS_PER_SEC << " seconds" << endl;

	if (output != "no_path")	cv::imwrite(output.c_str(), img);

	if (!no_show){
		cv::namedWindow(model.c_str(), cv::WINDOW_NORMAL);
		cv::imshow(model.c_str(), img);
		cv::waitKey(0);
		cv::destroyWindow(model.c_str());
	}

	return 0;
}
