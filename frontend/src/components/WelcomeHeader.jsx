import { geistMono, geistSans } from "@/assets/fonts";

const header = () => (
  <div className={"flex flex-col items-start justify-start"}>
    <h1 className={ `${geistMono.variable} antialiased text-4xl font-bold text-center` }>Muse</h1>
    <p className={`${geistMono.variable} ${geistSans.variable} font-extralight`}>
      For all of those music freaks out there.
    </p>

    <div className={`play-card`}>
      <p className={"antialiased text-2xl"}>Play</p>
    </div>
  </div>
);

export default header;
