import os

class Path:
    def __init__(self, args):
        self.data = f'../../../data/{args.dataset}/'
        self.misc = f'../../../misc/{args.dataset}/'
        self.emb = f'../../../misc/{args.dataset}/emb/'
        self.satistic = f'../../../confid_abla/{args.dataset}/'
        self.output = f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/no_sw'

        if args.abla_exp == True:
            self.output = f'../../../output/KGPH/{args.dataset}/abla_exp_no_sw/'
        # elif args.wide_deep == False: 
        #     self.output = f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/no_sw/cnn'

        if args.top_k == True:
            self.output = f"{self.output}/topk/"

        self.check_dir(f'../../../output/')
        self.check_dir(f'../../../output/KGPH/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/no_sw/')

        self.check_dir(self.data)
        self.check_dir(f'../../../misc/')
        self.check_dir(self.misc)
        self.check_dir(self.emb)
        self.check_dir(f'../../../confid_abla/')
        self.check_dir(self.satistic)
        self.check_dir(self.output)

    def check_dir(self, p):
        if not os.path.isdir(p):
            os.mkdir(p)

class Path_SW:
    def __init__(self, args):
        self.data = f'../../../data/{args.dataset}/'
        self.misc = f'../../../misc/{args.dataset}/'
        self.emb = f'../../../misc/{args.dataset}/emb/'
        self.satistic = f'../../../confid_abla/{args.dataset}/'
        self.output = f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/sw/'

        if args.abla_exp == True:
            self.output = f'../../../output/KGPH/{args.dataset}/abla_exp_no_sw/'
        # elif args.wide_deep == False: 
        #     self.output = f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/no_sw/cnn'

        if args.top_k == True:
            self.output = f"{self.output}/topk/"

        self.check_dir(f'../../../output/')
        self.check_dir(f'../../../output/KGPH/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/')
        self.check_dir(f'../../../output/KGPH/{args.dataset}/KGPH_p0{args.p_hop}_h_{args.h_hop}/sw/')
        self.check_dir(self.data)
        self.check_dir(f'../../../misc/')
        self.check_dir(self.misc)
        self.check_dir(self.emb)
        self.check_dir(f'../../../confid_abla/')
        self.check_dir(self.satistic)
        self.check_dir(self.output)

    def check_dir(self, p):
        if not os.path.isdir(p):
            os.mkdir(p)
