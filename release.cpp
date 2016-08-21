#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/core/utility.hpp>
#include "opencv2/imgcodecs.hpp"
#include <opencv2/highgui.hpp>
#include <iostream>
#include <complex>
#include <string>

using namespace std;

int main(int argc, char const *argv[]){

	// char* model, color, show, output;
	// int thresold, limit, width, heigth;
	// double zoom;
	// complex <double> constant;
	// for (int i=1; i<argc; i++){
	// 	if (argv[i] == "-m") model = argv[i + 1];
	// 	else if (argv[i] == "-c"){
	// 		constant.real(argv[i + 1]);
	// 		constant.imag(argv[i + 2]);
	// 	}
	// 	else if (argv[i] == "-t") threshold = argv[i + 1];
	// 	else if (argv[i] == "-l") limit = argv[i + 1];
	// 	else if (argv[i] == "-s"){
	// 		width = argv[i + 1];
	// 		height = argv[i + 2];
	// 	}
	// 	else if (argv[i] == "-z") zoom = argv[i + 1];
	// 	else if (argv[i] == "-r") color = argv[i + 1];
	// 	else if (argv[i] == "-w") show = argv[i + 1];
	// 	else if (argv[i] == "-o") output = argv[i + 1];
	// }

	int width = 1000;
	int height = 800;
	double zoom = 0.6;
	cv::Mat img(height, width, CV_32S);
	complex <double> z;
	complex <double> constant(0, -0.8);
	double re, im;

	for (int i=0; i<width; i++){
		re = (i - (width * 0.5)) / (0.5 * width * zoom);
		for (int j=0; j<height; j++){
			im = -(j - (height * 0.5)) / (0.5 * height * zoom);
			z.real(re);
			z.imag(im);
			int intensity = 0;
			while ((abs(z) < 2) && (intensity < 1000)){
				z = z * z + constant;
				intensity++;
			}
			img.at<int>(j, i) = intensity;
		}
	}

	img.convertTo(img, CV_8U);
	cv::applyColorMap(img, img, 11);

	cv::namedWindow("fractal", cv::WINDOW_NORMAL);
	cv::imshow("fractal", img);
	cv::waitKey(0);
	cv::destroyWindow("fractal");

	return 0;
}
