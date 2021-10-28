import math


def calculate_bit_rate(BW, sf, CR):
    return (BW / (2 ** sf)) * sf * CR


def calculate_time_on_air(pl, sf, cr, bw):
    N_pl = 8 + max(math.ceil(((8 * pl - 4 * sf + 44) / (4 * (sf - 2)))) * (cr + 4), 0)

    T_pl = N_pl * (2 ** sf) / bw
    T_pre = 12.25 * (2 ** sf) / bw
    return T_pl + T_pre


def calculate_snr(SNR0, sf):
    mw = SNR0 / (2 ** sf)
    return 10 * math.log(mw, 10)


if __name__ == "__main__":
    CR = float(input("enter code rate: "))
    payload = float(input("enter payload: "))
    SNR0 = float(input("enter SNR 0: "))

    for bandwidth in (125, 250, 500):
        print("for bandwidth", str(bandwidth)+"kHz")
        print("sf \t bit rate \t sensitivity \t ToA \t SNR")
        for sf in range(7, 13):
            bit_rate = calculate_bit_rate(bandwidth, sf, CR)
            time_on_air = calculate_time_on_air(payload, sf, CR, bandwidth)
            snr = calculate_snr(SNR0, sf)
            receiving_sensitivity = -168 + 10 * math.log(bandwidth*1000, 10) + snr
            print(sf, "\t", str(math.ceil(bit_rate * 100) / 100)+"kbps", "\t", math.ceil(receiving_sensitivity * 100) / 100, "\t",
                  str(math.ceil(time_on_air * 100) / 100)+"ms", "\t", math.ceil(snr * 100) / 100)
