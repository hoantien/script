#include <stdio.h>
#include <stdint.h>
#define VT_PIX_CLK (220000000)
//todo:read the LLPCLK (line_length_pclk) from register 0x342
#define LINE_LENGTH_PCLK_REG_ADDR		0x0342
#define LINE_LENGTH_PCLK_13M			(0x3000 / 2)
#define LINE_LENGTH_PCLK_1080P			(0x176C / 2)
#define LINE_LENGTH_PCLK_LONG_EXP		0x7FF0

//todo: read frame_length_lines form register REG=0x0340
#define FRAME_LENGTH_LINES_REG_ADDR		0x0340
#define FRAME_LENGTH_LINES_13M			0xDFC
#define FRAME_LENGTH_LINES_1080P		0xE55
#define FRAME_LENGTH_LINES_LONG_EXP		0x53E
#define CONVERT_TO_PLL(ll_pclk, x) (uint64_t)(((x) * VT_PIX_CLK / (ll_pclk)) / 1000000000)
uint16_t line_length_pclk;
uint16_t frame_length_lines;
uint64_t exposure_time[] = {31250,62500,125000,250000,500000,1000000,2000000,4000000,8000000,16666666.67,33333333.33,66666666.67,125000000,250000000,500000000,1000000000,2000000000,4000000000};
uint64_t exposure_time_t;
int main()
{
    for (int i=0; i<(sizeof(exposure_time)/sizeof(exposure_time[0])); i++)
    {
        if (exposure_time[i] >= 1000000000 ) // 1.0 seconds in nanoseconds
        {
            line_length_pclk = LINE_LENGTH_PCLK_LONG_EXP;
            frame_length_lines = FRAME_LENGTH_LINES_LONG_EXP;

        }
        else
        {
            line_length_pclk = LINE_LENGTH_PCLK_13M;
            frame_length_lines = FRAME_LENGTH_LINES_13M;
        }
        exposure_time_t = CONVERT_TO_PLL(line_length_pclk, exposure_time[i]);

        printf("%d\t",exposure_time[i]);
        printf("%x\n\r",exposure_time_t);
    }
    return 0;
}
